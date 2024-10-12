import cv2
import streamlit as st
from PIL import Image
from io import BytesIO
import img2pdf
import numpy as np
import random
import requests
from datetime import datetime

def generate_certificate():
    equipment_tested_choices = ["11 KV INDOOR VOLTAGE TRANSFORMER-P.T. (Epoxy Resin Type)",
                                "11 KV CURRENT TRANSFORMER-C.T (Epoxy Resin Type)",
                                "LOW TENSION- L.T. C.T (Epoxy Resin Type)",
                                "11 kV CT PT Combined Metering Unit"]
    
    specifications_choices = ["The Following Routine Test conforming to IS:16227 (1 & 3)",
                              "The Following Routine Test conforming to IS:16227 (1 & 2)",
                              "The Following Routine Test conforming to IS:2705/1992",
                              "The Following Routine Test conforming to IS:2705/1992 & 3156/1992"]
    
    image_urls = [
    "https://github.com/VAMPAR10/Certificate-Genereator/blob/master/PT.jpg",
    "https://github.com/VAMPAR10/Certificate-Genereator/blob/master/CT_page-0001.jpg",
    "https://github.com/VAMPAR10/Certificate-Genereator/blob/master/CPT_page-0001.jpg"
    ]   
    
    images = []
    for url in image_urls:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        images.append(img)

    burden_choices = ["2.5VA", "5VA", "10VA", "15VA"]
    accuracy_choices = ["0.1","0.2s", "0.2", "0.5", "0.5s", "1","3"]

    st.title("Certificate Generator")
    
    template_names = ["PT", "CT", "CPT"]
    template_ctpt_file = st.selectbox("Select a certificate template:", template_names)
    #template_ctpt_file = st.file_uploader("Upload the certificate template:", type=["jpg", "png"])
    
    equipment_tested = st.selectbox("Select equipment tested:", equipment_tested_choices)
    customer_name = st.text_input("Enter customer name:")

    if template_ctpt_file is not None:
        file_bytes = np.asarray(bytearray(template_ctpt_file.read()), dtype=np.uint8)
        template_ctpt = cv2.imdecode(file_bytes, 1)
    
        equipment_tested_to_specifications = dict(zip(equipment_tested_choices, specifications_choices))
        specifications = equipment_tested_to_specifications[equipment_tested]
        current_date = datetime.now().date()
        current_date_str = current_date.strftime("%Y-%m-%d")
        
        if equipment_tested == equipment_tested_choices[2]:
            rated_voltage = "415 KV"
            hsv = None
            ilv = "0.66 KV"
        else:
            rated_voltage = "11 KV"
            hsv = "12 KV"
            ilv = "28 kV/ 75 kVp"
        
        if equipment_tested == equipment_tested_choices[3]:
            transformer_ratio = "250/5A"
            burden_l = st.selectbox("Select burden (C):", burden_choices)
            burden_r = st.selectbox("Select burden (V):", burden_choices)
            accuracy_class_l = st.selectbox("Select accuracy class (C):", accuracy_choices)
            accuracy_class_r = st.selectbox("Select accuracy class (V):", accuracy_choices)
            accuracy_class = accuracy_class_l
            burden = burden_l
            
        else:
            if equipment_tested == equipment_tested_choices[0]:
                transformer_ratio = "11000/110 V"
            else:
                transformer_ratio = st.text_input("Enter transformer ratio:")
                        
            burden = st.selectbox("Select burden:", burden_choices)
            accuracy_class = st.selectbox("Select accuracy class:", accuracy_choices) 

        if equipment_tested == equipment_tested_choices[0]:
            stc = None
        else: 
            stc = st.text_input("Enter S.T.C:")
            
        frequency = "50 Hz"
        
        serial_num = st.text_input("Enter Equipment Serial Number:")
        
        if equipment_tested == equipment_tested_choices[1] or equipment_tested_choices[2] or equipment_tested_choices[3]:
            if accuracy_class == accuracy_choices[1] or accuracy_choices[2]:
                perccent_voltage_error_1 = [str(round(random.uniform(-0.75, 0.75), 3)) for _ in range(6)]
                phase_displacement_minutes_1 =  [str(round(random.uniform(0, 30.0), 2)) for _ in range(6)]
                perccent_voltage_error_5 =  [str(round(random.uniform(-0.35, 0.35), 3)) for _ in range(6)]
                phase_displacement_minutes_5 =  [str(round(random.uniform(0, 15.0), 2)) for _ in range(6)]
                perccent_voltage_error_20 =  [str(round(random.uniform(-0.2, 0.2), 3)) for _ in range(6)]
                phase_displacement_minutes_20 =  [str(round(random.uniform(0, 10.0), 2)) for _ in range(6)]
                perccent_voltage_error_100 =  [str(round(random.uniform(-0.2, 0.2), 3)) for _ in range(6)]
                phase_displacement_minutes_100 =  [str(round(random.uniform(0, 10.0), 2)) for _ in range(6)]
                perccent_voltage_error_120 = [str(round(random.uniform(-0.2, 0.2), 3)) for _ in range(6)]
                phase_displacement_minutes_120 = [str(round(random.uniform(0, 10.0), 2)) for _ in range(6)]
            if accuracy_class == accuracy_choices[3] or accuracy_choices[4]:
                perccent_voltage_error_1 = [str(round(random.uniform(-1.5, 1.5), 3)) for _ in range(6)]
                phase_displacement_minutes_1 = [str(round(random.uniform(0, 90.0), 2)) for _ in range(6)]
                perccent_voltage_error_5 = [str(round(random.uniform(-0.75, 0.75), 3)) for _ in range(6)]
                phase_displacement_minutes_5 = [str(round(random.uniform(0, 45.0), 2)) for _ in range(6)]
                perccent_voltage_error_20 = [str(round(random.uniform(-0.5, 0.5), 3)) for _ in range(6)]
                phase_displacement_minutes_20 = [str(round(random.uniform(0, 30.0), 2)) for _ in range(6)]
                perccent_voltage_error_100 = [str(round(random.uniform(-0.5, 0.5), 3)) for _ in range(6)]
                phase_displacement_minutes_100 = [str(round(random.uniform(0, 30.0), 2)) for _ in range(6)]
                perccent_voltage_error_120 = [str(round(random.uniform(-0.5, 0.5), 3)) for _ in range(6)]
                phase_displacement_minutes_120 = [str(round(random.uniform(0, 30.0), 2)) for _ in range(6)]
            
        if equipment_tested == equipment_tested_choices[0]:
            if accuracy_class == accuracy_choices[0]:
                perccent_voltage_error = [str(round(random.uniform(-0.1, 0.1), 3)) for _ in range(18)]
                phase_displacement_minutes = [str(round(random.uniform(0, 5.0), 2)) for _ in range(18)]
                crads = [str(round(random.uniform(0, 0.2), 3)) for _ in range(18)]
            elif accuracy_class == accuracy_choices[2]:
                perccent_voltage_error = [str(round(random.uniform(-0.2, 0.2), 3)) for _ in range(18)]
                phase_displacement_minutes = [str(round(random.uniform(0, 10.0), 2)) for _ in range(18)]
                crads = [str(round(random.uniform(0, 0.2), 3)) for _ in range(18)]
            elif accuracy_class == accuracy_choices[3]:
                perccent_voltage_error = [str(round(random.uniform(-0.5, 0.5), 3)) for _ in range(18)]
                phase_displacement_minutes = [str(round(random.uniform(0, 20.0), 2)) for _ in range(18)]
                crads = [str(round(random.uniform(0, 0.2), 3)) for _ in range(18)]
            elif accuracy_class == accuracy_choices[5]:
                perccent_voltage_error = [str(round(random.uniform(-1.0, 1.0), 3)) for _ in range(18)]
                phase_displacement_minutes = [str(round(random.uniform(0, 40.0), 2)) for _ in range(18)]
                crads = [str(round(random.uniform(0, 0.2), 3)) for _ in range(18)]
            elif accuracy_class == accuracy_choices[6]:
                perccent_voltage_error = [str(round(random.uniform(-3.0, 3.0), 3)) for _ in range(18)]
                phase_displacement_minutes = ["-"] * 6  
                crads = [str(round(random.uniform(0, 0.2), 3)) for _ in range(18)]                 

    if st.button("Generate Certificate"):
        # Write for PT Certificates
        if equipment_tested == equipment_tested_choices[0]:
          cv2.putText(template_ctpt, equipment_tested, (845, 675), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, customer_name, (845, 725), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, specifications, (845, 835), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)  
          cv2.putText(template_ctpt, transformer_ratio, (845, 890), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)  
          cv2.putText(template_ctpt, rated_voltage, (845, 945), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, ilv, (845, 1000), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (845, 1050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, accuracy_class, (845, 1105), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, frequency, (845, 1160), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, "1.2 TIMES CONT. & 1.5 FOR 30 SEC.", (845, 1215), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, serial_num, (210, 2300), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (655, 2140), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (655, 2300), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (655, 2470), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, current_date_str, (310, 2795), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          
          # percent_voltage_error
          cv2.putText(template_ctpt, perccent_voltage_error[1], (1100, 2090), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[2], (1320, 2090), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[3], (1545, 2090), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[4], (1770, 2090), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[5], (1980, 2090), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[0], (2200, 2090), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[6], (1100, 2255), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[7], (1320, 2255), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[8], (1545, 2255), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[9], (1770, 2255), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[10], (1980, 2255), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[11], (2200, 2255), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[12], (1100, 2420), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[13], (1320, 2420), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[14], (1545, 2420), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[15], (1770, 2420), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[16], (1980, 2420), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[17], (2200, 2420), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)

          # phase_displacement_minutes
          cv2.putText(template_ctpt, phase_displacement_minutes[1], (1100, 2145), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[2], (1320, 2145), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[3], (1545, 2145), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[4], (1770, 2145), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[5], (1980, 2145), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[0], (2200, 2145), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[6], (1100, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[7], (1320, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[8], (1545, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[9], (1770, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[10], (1980, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[11], (2200, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[12], (1100, 2475), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[13], (1320, 2475), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[14], (1545, 2475), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[15], (1770, 2475), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[16], (1980, 2475), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[17], (2200, 2475), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)

          # crads
          cv2.putText(template_ctpt, crads[1], (1100, 2200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[2], (1320, 2200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[3], (1545, 2200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[4], (1770, 2200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[5], (1980, 2200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[0], (2200, 2200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[1], (1100, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[2], (1320, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[3], (1545, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[4], (1770, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[5], (1980, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[0], (2200, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[1], (1100, 2530), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[2], (1320, 2530), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[3], (1545, 2530), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[4], (1770, 2530), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[5], (1980, 2530), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, crads[0], (2200, 2530), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        
        # Write for CT Certificates
        if equipment_tested == equipment_tested_choices[1]:
          cv2.putText(template_ctpt, equipment_tested, (800, 680), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, customer_name, (800, 730), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, specifications, (800, 840), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)  
          cv2.putText(template_ctpt, transformer_ratio, (800, 890), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)  
          cv2.putText(template_ctpt, rated_voltage, (800, 940), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, ilv, (800, 990), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (800, 1045), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, accuracy_class, (800, 1095), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, frequency, (800, 1150), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, stc, (800, 1200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, serial_num, (210, 2045), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, serial_num, (210, 2200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, serial_num, (210, 2360), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, transformer_ratio, (505, 2045), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, transformer_ratio, (505, 2200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, transformer_ratio, (505, 2360), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (660, 2040), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (660, 2200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (660, 2360), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, current_date_str, (310, 2675), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          
          cv2.putText(template_ctpt, perccent_voltage_error_120[0], (1050, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[0], (1185, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[0], (1315, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[0], (1445, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[0], (1575, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[1], (1705, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[1], (1840, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[1], (1970, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[1], (2100, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[1], (2235, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[2], (1050, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[2], (1185, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[2], (1315, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[2], (1445, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[2], (1575, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[3], (1705, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[3], (1840, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[3], (1970, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[3], (2100, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[3], (2235, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[4], (1050, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[4], (1185, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[4], (1315, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[4], (1445, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[4], (1575, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[5], (1705, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[5], (1840, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[5], (1970, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[5], (2100, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[5], (2235, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          
          cv2.putText(template_ctpt, phase_displacement_minutes_120[0], (1055, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[0], (1190, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[0], (1320, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[0], (1450, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[0], (1580, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[1], (1710, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[1], (1845, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[1], (1975, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[1], (2105, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[1], (2240, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[2], (1055, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[2], (1190, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[2], (1320, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[2], (1450, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[2], (1580, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[3], (1710, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[3], (1845, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[3], (1975, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[3], (2105, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[3], (2240, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[4], (1055, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[4], (1190, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[4], (1320, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[4], (1450, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[4], (1580, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[5], (1710, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[5], (1845, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[5], (1975, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[5], (2105, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[5], (2240, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          
        # Write for LT CT Certificates
        if equipment_tested == equipment_tested_choices[2]:
          cv2.putText(template_ctpt, equipment_tested, (800, 680), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, customer_name, (800, 730), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, specifications, (800, 840), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)  
          cv2.putText(template_ctpt, transformer_ratio, (800, 890), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)  
          cv2.putText(template_ctpt, rated_voltage, (800, 940), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, ilv, (800, 990), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (800, 1045), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, accuracy_class, (800, 1095), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, frequency, (800, 1150), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, stc, (800, 1200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, serial_num, (210, 2045), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, serial_num, (210, 2200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, serial_num, (210, 2360), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, transformer_ratio, (505, 2045), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, transformer_ratio, (505, 2200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, transformer_ratio, (505, 2360), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (660, 2040), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (660, 2200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (660, 2360), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, current_date_str, (310, 2675), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          
          cv2.putText(template_ctpt, perccent_voltage_error_120[0], (1050, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[0], (1185, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[0], (1315, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[0], (1445, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[0], (1575, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[1], (1705, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[1], (1840, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[1], (1970, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[1], (2100, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[1], (2235, 1995), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[2], (1050, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[2], (1185, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[2], (1315, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[2], (1445, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[2], (1575, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[3], (1705, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[3], (1840, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[3], (1970, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[3], (2100, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[3], (2235, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[4], (1050, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[4], (1185, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[4], (1315, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[4], (1445, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[4], (1575, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[5], (1705, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[5], (1840, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[5], (1970, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[5], (2100, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[5], (2235, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          
          cv2.putText(template_ctpt, phase_displacement_minutes_120[0], (1055, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[0], (1190, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[0], (1320, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[0], (1450, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[0], (1580, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[1], (1710, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[1], (1845, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[1], (1975, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[1], (2105, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[1], (2240, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[2], (1055, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[2], (1190, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[2], (1320, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[2], (1450, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[2], (1580, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[3], (1710, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[3], (1845, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[3], (1975, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[3], (2105, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[3], (2240, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[4], (1055, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[4], (1190, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[4], (1320, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[4], (1450, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[4], (1580, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[5], (1710, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[5], (1845, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[5], (1975, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[5], (2105, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[5], (2240, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        
        # Write for CPT Certificates
        if equipment_tested == equipment_tested_choices[3]:
          cv2.putText(template_ctpt, equipment_tested, (825, 470), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, customer_name, (825, 520), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, serial_num, (825, 570), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, specifications, (825, 620), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, rated_voltage, (825, 670), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, ilv, (825, 720), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)  
          cv2.putText(template_ctpt, frequency, (825, 770), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, transformer_ratio, (825, 870), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)  
          cv2.putText(template_ctpt, transformer_ratio, (1625, 870), 0, 1, (0, 0, 0), 2, cv2.LINE_AA) 
          cv2.putText(template_ctpt, burden_l, (825, 920), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden_r, (1625, 920), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, accuracy_class_l, (825, 970), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, accuracy_class_r, (1625, 970), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, stc, (825, 1020), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, "1.2 TIMES CONT. & 1.5 FOR 30 SEC.", (1625, 1065), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (570, 2000), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (570, 2105), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (570, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (500, 2515), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (500, 2615), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, burden, (500, 2725), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, current_date_str, (470, 3040), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          
          cv2.putText(template_ctpt, perccent_voltage_error_120[0], (1125, 1975), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[0], (1245, 1975), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[0], (1370, 1975), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[0], (1495, 1975), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[0], (1620, 1975), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[1], (1740, 1975), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[1], (1865, 1975), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[1], (1990, 1975), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[1], (2115, 1975), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[1], (2240, 1975), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[2], (1125, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[2], (1245, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[2], (1370, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[2], (1495, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[2], (1620, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[3], (1740, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[3], (1865, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[3], (1990, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[3], (2115, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[3], (2240, 2155), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[4], (1125, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[4], (1245, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[4], (1370, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[4], (1495, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[4], (1620, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_120[5], (1740, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_100[5], (1865, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_20[5], (1990, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_5[5], (2115, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error_1[5], (2240, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          
          cv2.putText(template_ctpt, phase_displacement_minutes_120[0], (1055, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[0], (1190, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[0], (1320, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[0], (1450, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[0], (1580, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[1], (1710, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[1], (1845, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[1], (1975, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[1], (2105, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[1], (2240, 2050), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[2], (1055, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[2], (1190, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[2], (1320, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[2], (1450, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[2], (1580, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[3], (1710, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[3], (1845, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[3], (1975, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[3], (2105, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[3], (2240, 2205), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[4], (1055, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[4], (1190, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[4], (1320, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[4], (1450, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[4], (1580, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_120[5], (1710, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_100[5], (1845, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_20[5], (1975, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_5[5], (2105, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes_1[5], (2240, 2365), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          
          cv2.putText(template_ctpt, perccent_voltage_error[1], (1100, 2090), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[2], (1320, 2090), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[3], (1545, 2090), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[4], (1770, 2090), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[5], (1980, 2090), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[0], (2200, 2090), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[6], (1100, 2255), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[7], (1320, 2255), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[8], (1545, 2255), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[9], (1770, 2255), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[10], (1980, 2255), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[11], (2200, 2255), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[12], (1100, 2420), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[13], (1320, 2420), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[14], (1545, 2420), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[15], (1770, 2420), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[16], (1980, 2420), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, perccent_voltage_error[17], (2200, 2420), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)

          # phase_displacement_minutes
          cv2.putText(template_ctpt, phase_displacement_minutes[1], (1100, 2145), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[2], (1320, 2145), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[3], (1545, 2145), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[4], (1770, 2145), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[5], (1980, 2145), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[0], (2200, 2145), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[6], (1100, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[7], (1320, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[8], (1545, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[9], (1770, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[10], (1980, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[11], (2200, 2310), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[12], (1100, 2475), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[13], (1320, 2475), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[14], (1545, 2475), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[15], (1770, 2475), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[16], (1980, 2475), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          cv2.putText(template_ctpt, phase_displacement_minutes[17], (2200, 2475), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
          
        # cv2.putText(template_ctpt, equipment_tested, (960, 660), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        # cv2.putText(template_ctpt, customer_name, (960, 710), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        # cv2.putText(template_ctpt, specifications, (960, 760), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # if equipment_tested == equipment_tested_choices[3]:
        #     cv2.putText(template_ctpt, transformer_ratio, (960, 915), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, "11 KV/ 110 V", (1600, 915), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, rated_voltage, (960, 960), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, rated_voltage, (1600, 960), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, hsv, (960, 1010), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, hsv, (1600, 1010), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, burden_l, (960, 1060), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, burden_r, (1600, 1060), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, accuracy_class_l, (960, 1100), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, accuracy_class_r, (1600, 1100), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, ilv, (960, 1150), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, ilv, (1600, 1150), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, frequency, (960, 1200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, frequency, (1600, 1200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, stc, (960, 1245), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, "1.2 TIMES CONT. & 1.5 FOR 30 SEC.", (1600, 1300), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        # else:
        #     cv2.putText(template_ctpt, transformer_ratio, (960, 875), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, rated_voltage, (960, 925), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, hsv, (960, 975), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, burden, (960, 1035), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, accuracy_class, (960, 1100), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, ilv, (960, 1150), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, frequency, (960, 1200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     cv2.putText(template_ctpt, stc, (960, 1245), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        #     if equipment_tested == equipment_tested_choices[0]:
        #         cv2.putText(template_ctpt, "Voltage Factor", (360, 1300), 0, 1, (0, 0, 0), 3, cv2.LINE_AA)
        #         cv2.putText(template_ctpt, "1.2 TIMES CONT. & 1.5 FOR 30 SEC.", (960, 1300), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)

        st.write("Certificate generated!")

            
        # Encode image to bytes
        is_success, buffer = cv2.imencode(".jpg", template_ctpt)
        jpg_data = buffer.tobytes()

         # Convert image to PDF
        pdf_data = img2pdf.convert(jpg_data)
            
        # Provide download button
        st.download_button(
            label="Download Certificate as PDF",
            data=pdf_data,
            file_name="certificate.pdf",
            mime="application/pdf"
        )

generate_certificate()
