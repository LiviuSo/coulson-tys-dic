import streamlit as st
from PIL import Image
import pandas
import search


ti = st.text_input(label="Enter a Sanskrit work (IAST):", key="word_iast")

result_container = st.empty()

raw_word = st.session_state["word_iast"]

rgs = pandas.read_csv(filepath_or_buffer="dic-ranges.csv", sep="-")

# search for the dic page containing the word
found = False
for index, row in rgs.iterrows():  # todo improve algorithm
    word = raw_word.strip('\n').lower()
    if search.is_in_range(word.lower(), row['from'], row['to']):
        found = True
        # show the corresponding image
        image_name_root = f"{search.get_index_as_string(row['index'])}-{row['from']}-{row['to']}-{row['page']}"
        col1, empty, col2 = st.columns([2, 0.5, 2])
        with col1:
            image = Image.open(f"dic/{image_name_root}-A.png")
            st.image(image, caption=f"Range: {row['from']} - {row['to']}")
        with col2:
            image = Image.open(f"dic/{image_name_root}-B.png")
            st.image(image)
        break

# show placeholder if not found
if not found:
    image = Image.open("placeholder.png")
    result_container.image(image, caption="Page containing the word")
