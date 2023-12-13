#USE CUDAENV ANACONDA ENVIRONMENT!!!!!!!
import streamlit as st
import pandas as pd
import bz2
import pickle
import _pickle
import base64
from PIL import Image
import os

model_namee = "lr_fraud_model.pkl"
here = os.path.dirname(os.path.abspath(__file__))
model_name = os.path.join(here, model_namee)
model=pickle.load(open(model_name , "rb"))

st.set_page_config(page_title='Fraud Detection', layout='wide')
home, findings, detect_fraud, contact= st.tabs(["Home", "Findings", "Detect Fraud", "Contact Us!"])
with home:
	def get_base64(bin_file):
		with open(bin_file, 'rb') as f:
			data = f.read()
		return base64.b64encode(data).decode()

	def set_background(png_file):
        	bin_str = get_base64(png_file)
        	page_bg_img = '''
        	<style>
        	.stApp {
        	background-image: url("data:image/png;base64,%s");
        	background-size: cover;
        	}
        	</style>
        	''' % bin_str
        	st.markdown(page_bg_img, unsafe_allow_html=True)
	background_home = os.path.join(here, "smaller.png")
	set_background(background_home)
	st.title('How to detect fraud?')
	st.write("This website will help you detect fradulant behaviour on credit card transactions.")
	with st.container():
		st.write("---")
		st.markdown(" ## What you need to do: ")
		st.write("""
- ### Go to the *Detect Fraud* tab.
- ### Fill the required information.
- ### Click the *Predict* button to check if the transaction is fradulant or not.

""") 
with findings:
	with st.container():
		st.write("---")
		st.markdown("### Important Insights:")
		st.write("---")
		img_path = os.path.join(here, "piechart.png")
		img_activity = Image.open(img_path)
		st.caption('\t\tRatio of Real VS Fraud Transactions in our Dataset.')
		st.image(img_activity , caption = '')
		st.write("There is huge imbalance between frauds and real transactions.")
		st.write("---")
		left_column_finding, right_column_finding = st.columns(2)
		with left_column_finding:
			st.write("---")
			img_path2 = os.path.join(here, "displotdark.png")
			img_activity2 = Image.open(img_path2)
			st.caption('\t\tTransaction activities during the span of two days.')
			st.image(img_activity2 , caption = '')
			st.write("Assuming data was collected at 12:00 AM, Most transactions happened from 6:00 AM to 10:00 PM. After that,the number of transactions dropped significantly from 11:00 PM TO 6:00 AM the next day.")
			img_path3 = os.path.join(here, "fraudisplot.png")
			img_activity3 = Image.open(img_path3)
			st.caption('\t\tFradulant transaction activities during the span of two days.')
			st.image(img_activity3, caption = '')
		#with left_column_finding:
			st.write("Fradulant transaction activities follow the same pattern as real transactions.")
with detect_fraud:

	with st.container():
		st.write("---")
		left_column, right_column = st.columns(2)
		with left_column:
			st.markdown("### Only authorized employees know the meaning behind V values")
			st.write("---")
			v7 = st.number_input("Insert V7 value", min_value=0.0)
			st.write("##")
			v10 = st.number_input("Insert V10 value", min_value=0.0)
			st.write("##")
			v12 = st.number_input("Insert V12 value", min_value=1.0)
			st.write("##")
			v14 = st.number_input("Insert V14 value", min_value=0.0)
			st.write("##")
			v17 = st.number_input("Insert V17 value", min_value=1.0)
		
			obs = {'V7':v7, 'V10':v10, 'V12':v12, 'V14':v14, 'V17':v17}
			observation = pd.DataFrame([obs])
	with st.container():
		st.write("---")
		st.write("##")
		predict = st.button("Predict")
		st.markdown("""
<style>
.stButton>button {
  display: inline-block;
  padding: 15px 25px;
  font-size: 24px;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  color: #fff;
  background-color: #FB8B24;
  border: none;
  border-radius: 15px;
  box-shadow: 0 9px #999;
}

.stButton>button:hover {background-color: #FB8B24}

.stButton>button:active {
  text-align: center;
  text-decoration: none;
  outline: none;
  color: #fff;
  background-color: #E36414;
  box-shadow: 0 5px #666;
  transform: translateY(4px);
}
</style>

""", unsafe_allow_html=True)
		result = model.predict(observation)
		result_value = int(result[0])
		proba = model.predict_proba(observation)
		proba = (round(proba[0][result_value], 2))*100
		proba = str(proba)
		
		intt = 0
		if predict:
			if result_value==1:
				fs = 20
				message = "The system detected fraudulant activities with a confidence of "+proba+"%."
				html_str = f"""
<style>
p.a {{
  font: bold {fs}px Courier;
}}
</style>
<p class="a"; style="background-color:none;">{message}</p>
"""

				st.markdown(html_str, unsafe_allow_html=True)
			else:
				fs = 20
				message = "No fradulant activities detected with a confidence of "+proba+"%."
				html_str = f"""
<style>
p.a {{
  font: bold {fs}px Courier;
}}
</style>
<p class="a"; style="background-color:none;">{message}</p>
"""
				st.markdown(html_str, unsafe_allow_html=True)

with contact:
	# Header for the team section
	st.header("Team Members :man-man-boy-boy:")
	# Sample data for 8 team members
	team_members = [
    		{"name": "Fai", "occupation": "Computer Science", "linkedin": "https://www.linkedin.com/in/fai-alamri-121747211/"},
    		{"name": "Abeer", "occupation": "Computer Science", "linkedin": "https://www.linkedin.com/in/abeer-alsafraa/"},
    		{"name": "Areej", "occupation": "Computer Engineer", "linkedin": "https://www.linkedin.com/in/areej-alghamdi-38a270202/"},
    		{"name": "Renad", "occupation": "Artificial Intelligence", "linkedin": "https://www.linkedin.com/in/renad-felemban/"},
    		{"name": "Hessah", "occupation": "AI Engineer", "linkedin": "https://www.linkedin.com/in/hesahalharbi/"},
    		{"name": "Alenizy", "occupation": "Computer Science", "linkedin": "https://www.linkedin.com/in/abdulrahman-alenizy-51150a220/"},
    		{"name": "Rakan", "occupation": "Computer Engineer", "linkedin": "https://www.linkedin.com/in/ralbadeen/"},
    		{"name": "Osama", "occupation": "Artificial Intelligence", "linkedin": "https://www.linkedin.com/in/oddissblue/"}
		]
	# Style improvements with custom CSS
	st.markdown("""
    <style>
    .team-card {
        margin: 10px;
        border-radius: 10px;
        background-color: #1E1E1E; /* Dark background for the card */
        color: #FFFFFF; /* White text color */
        padding: 10px;
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3); /* More pronounced shadow */
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        display: flex; /* Use flex layout */
        flex-direction: column; /* Stack elements vertically */
        align-items: center; /* Center-align items for a neat look */
        justify-content: center; /* Center content vertically */
    }
    .team-card img {
        border-radius: 50%; /* Circular images */
        width: 80px; /* Fixed width, adjust as needed */
        height: 80px; /* Fixed height, adjust as needed */
        object-fit: cover; /* Ensure the image covers the area */
        border: 2px solid #0077B5; /* Border color similar to LinkedIn's color */
        margin-bottom: 10px; /* Space between image and text */
    }
    .team-card h4 {
        margin: 10px 0 5px 0; /* Spacing for name */
        font-size: 18px; /* Larger font size for name */
    }
    .team-card p {
        margin: 0; /* Remove margin from paragraph for tighter spacing */
        font-size: 14px; /* Smaller font size for occupation */
    }
    .linkedin-button {
        margin-top: 15px; /* More space above the button */
        padding: 10px 15px; /* Larger padding for a bigger button */
        font-weight: bold; /* Make button text bold */
        border: none; /* Remove border */
        outline: none; /* Remove outline */
        text-transform: uppercase; /* Uppercase button text */
        letter-spacing: 1px; /* Add spacing between letters */
        transition: background-color 0.3s ease-in-out; /* Smooth background color transition on hover */
        cursor: pointer; /* Cursor to pointer to indicate clickable */
    }
    .team-card:hover {
        transform: scale(1.05); /* Slightly scale up cards on hover */
        box-shadow: 5px 5px 25px rgba(0, 0, 0, 0.5); /* Larger shadow on hover */
    }
    </style>
	""", unsafe_allow_html=True)
	# Function to create a team member card
	def create_team_member_card(member):
    	# Load the image from a local file as a data URL
		file_path = os.path.join(here, f"images\{member['name']}.jpeg")
    	
		with open(file_path, "rb") as file:
        		contents = file.read()
        		data_url = base64.b64encode(contents).decode("utf-8")
    	# Render the card with the team member's data
		st.markdown(f"""
    <div class="team-card">
        <img src="data:image/gif;base64,{data_url}" class="profile-img" alt="Profile image">
        <h4>{member['name']}</h4>
        <p>{member['occupation']}</p>
        <a href="{member['linkedin']}" target="_blank" class="linkedin-button">LinkedIn</a>
    </div>
    		""", unsafe_allow_html=True)
	# Display team members in groups of four
	for i in range(0, len(team_members), 4):
    		cols = st.columns(4)
    		for j in range(4):
        		with cols[j]:
            			if i+j < len(team_members):
                			create_team_member_card(team_members[i+j])
