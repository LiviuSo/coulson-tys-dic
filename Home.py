import streamlit as st
from PIL import Image
import pandas
import search

st.title("Michael Coulson's 'TYS' dictionary")
st.header("Sanskrit-English")

# todo generate csv file from filenames
rgs = pandas.read_csv(filepath_or_buffer="dic-ranges.csv", sep="-")

st.text_input(label="Enter a Sanskrit work (IAST):", key="word_iast")

result_container = st.empty()

word = st.session_state["word_iast"]

# search for the dic page containing the word
found = False
for index, row in rgs.iterrows():  # todo improve algorithm
    if search.is_in_range(word, row['from'], row['to']):
        found = True
        # show the corresponding image
        image_name = f"{search.get_index_as_string(row['index'])}-{row['from']}-{row['to']}-{row['page']}.png"
        image = Image.open(f"dic/{image_name}")
        result_container.image(image)
        break

# show placeholder if not found
if not found:
    image = Image.open("placeholder.png")
    result_container.image(image, caption="Page containing the word")
