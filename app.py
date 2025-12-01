# Fixing the f-string syntax that caused the error in the Streamlit markdown line

# Corrected Streamlit line
fixed_line = """st.markdown(f"**{row['Title']}** ({row['Source']}, {row['Publication Date']})  \\n"
                f"*Emotion:* {row['Emotion Label']} | *Theme:* {row['Thematic Label']}  \\n"
                f"[Read More]({row['URL']})  \\n"
                f"> {row['Summary']}")"""

# Replace the faulty code section with corrected one in app.py
app_path = "/mnt/data/witness_archive_app/app.py"
with open(app_path, "r") as file:
    lines = file.readlines()

with open(app_path, "w") as file:
    for line in lines:
        if "st.markdown(f\"**{row['Title']}**" in line:
            file.write(fixed_line + "\n")
        else:
            file.write(line)

app_path
