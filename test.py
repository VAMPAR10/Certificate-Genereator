import cv2
import streamlit as st
import img2pdf
import numpy as np

def generate_certificate():
    equipment_tested_choices = ["11 KV INDOOR VOLTAGE TRANSFORMER-P.T. (Epoxy Resin Type)",
                                "11 KV CURRENT TRANSFORMER-C.T (Epoxy Resin Type)",
                                "LOW TENSION- L.T. C.T (Epoxy Resin Type)",
                                "11 kV CT PT Combined Metering Unit"]
    
    specifications_choices = ["The Following Routine Test conforming to IS:16227 (1 & 3)",
                              "The Following Routine Test conforming to IS:16227 (1 & 2)",
                              "The Following Routine Test conforming to IS:2705/1992",
                              "The Following Routine Test conforming to IS:2705/1992 & 3156/1992"]
    
    burden_choices = ["2.5VA", "5VA", "10VA", "15VA"]
    accuracy_choices = ["0.2s", "0.2", "0.5", "0.5s", "1"]

    st.title("Certificate Generator")

    equipment_tested = st.selectbox("Select equipment tested:", equipment_tested_choices)
    customer_name = st.text_input("Enter customer name:")
    
    template_ctpt_file = st.file_uploader("Upload the certificate template:", type=["jpg", "png"])
    if template_ctpt_file is not None:
        file_bytes = np.asarray(bytearray(template_ctpt_file.read()), dtype=np.uint8)
        template_ctpt = cv2.imdecode(file_bytes, 1)
    
        equipment_tested_to_specifications = dict(zip(equipment_tested_choices, specifications_choices))
        specifications = equipment_tested_to_specifications[equipment_tested]

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

    if st.button("Generate Certificate"):
        cv2.putText(template_ctpt, equipment_tested, (960, 660), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(template_ctpt, customer_name, (960, 710), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(template_ctpt, specifications, (960, 760), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)

        if equipment_tested == equipment_tested_choices[3]:
            cv2.putText(template_ctpt, transformer_ratio, (960, 915), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, "11 KV/ 110 V", (1600, 915), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, rated_voltage, (960, 960), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, rated_voltage, (1600, 960), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, hsv, (960, 1010), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, hsv, (1600, 1010), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, burden_l, (960, 1060), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, burden_r, (1600, 1060), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, accuracy_class_l, (960, 1100), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, accuracy_class_r, (1600, 1100), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, ilv, (960, 1150), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, ilv, (1600, 1150), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, frequency, (960, 1200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, frequency, (1600, 1200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, stc, (960, 1245), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, "1.2 TIMES CONT. & 1.5 FOR 30 SEC.", (1600, 1300), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(template_ctpt, transformer_ratio, (960, 875), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, rated_voltage, (960, 925), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, hsv, (960, 975), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, burden, (960, 1035), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, accuracy_class, (960, 1100), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, ilv, (960, 1150), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, frequency, (960, 1200), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(template_ctpt, stc, (960, 1245), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)
            if equipment_tested == equipment_tested_choices[0]:
                cv2.putText(template_ctpt, "Voltage Factor", (360, 1300), 0, 1, (0, 0, 0), 3, cv2.LINE_AA)
                cv2.putText(template_ctpt, "1.2 TIMES CONT. & 1.5 FOR 30 SEC.", (960, 1300), 0, 1, (0, 0, 0), 2, cv2.LINE_AA)

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
