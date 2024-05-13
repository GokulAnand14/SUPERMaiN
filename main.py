import streamlit as st
from gradio_client import Client

st.set_page_config(
        page_title="supermAIn",
        page_icon="https://i.ibb.co/kcfZcsW/new-circle.png"
)

hide_St = """
	<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

st.markdown(hide_St, unsafe_allow_html=True)

def main():
    st.title("supermAIn")
    st.write("Enter image URL, Enter Prompt, Select Style, Click Generate and Get your Image")
    
    st.sidebar.header("Settings")
    image_urls = st.sidebar.text_area("Image URLs (comma-separated)", value="", height=100)
    with st.sidebar.expander("How to get the image URL"):
        st.write('''
            1. Go to https://postimages.org/ 🔗
            2. Upload your image ⬆
            3. Copy the "Direct link:" ©
            4. Repeat step 1-3 for all your images 🖼
            5. Paste those URLs above 👆
            
            or you can just "copy image link" from google :)
        ''')
    prompt = st.sidebar.text_input("Prompt", value="main img as an astronaut, profile picture, zoomed in, facing camera")
    negative_prompt = st.sidebar.text_input("Negative Prompt", value="bad quality, bad anatomy, worst quality, low quality, lowres, extra fingers, blur, blurry, ugly, wrong proportions, watermark, image artifacts, bad eyes")
    style_template = st.sidebar.selectbox("Style Template", ['(No style)', 'Cinematic', 'Disney Charactor', 'Digital Art', 'Photographic (Default)', 'Fantasy art', 'Neonpunk', 'Enhance', 'Comic book', 'Lowpoly', 'Line art'])
    num_sample_steps = st.sidebar.slider("Number of Sample Steps", min_value=20, max_value=100, value=60)
    style_strength = st.sidebar.slider("Style Strength (%)", min_value=15, max_value=50, value=10)
    num_output_images = st.sidebar.slider("Number of Output Images", min_value=1, max_value=4, value=1)
    guidance_scale = st.sidebar.slider("Guidance Scale", min_value=0.1, max_value=10.0, value=5.0)
    seed = st.sidebar.slider("Seed", min_value=0, max_value=2147483647, value=140609)
    
    if st.button("Generate"):
        st.write("⏳ PLEASE WAIT, IT MAY TAKE A LONG TIME ⏳")
        image_urls_list = [url.strip() for url in image_urls.split(",")]
        client = Client("https://tencentarc-photomaker-style.hf.space/--replicas/j9pup/")
        result = client.predict(
            image_urls_list,
            prompt,
            negative_prompt,
            style_template,
            num_sample_steps,
            style_strength,
            num_output_images,
            guidance_scale,
            seed,
            api_name="/generate_image"
        )
        
        st.page_link("https://twitter.com/not_gallium", label="🔵Follow me on 𝕏", icon="❎")
        st.page_link("https://youtube.com/@GAllium14", label="🔴Subscribe to my YT channel", icon="📺")
        st.page_link("https://github.com/GokulAnand14/SUPERMaiN", label="🌟Open-Source on GitHub", icon="🔓")
        st.page_link("https://huggingface.co/TencentARC/PhotoMaker", label="🖼Powered By TencentARC/PhotoMaker", icon="⚡")
        st.write("made with ❤ in INDIA🇮")

        # Extract image URLs from the result
        image_urls = [item['image'] for item in result[0]]
        
        # Display the images using st.image()
        for image_url in image_urls:
            st.image(image_url, caption=None, use_column_width=True)

if __name__ == "__main__":
    main()
