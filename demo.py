from gradio_client import Client



client = Client("https://tencentarc-photomaker-style.hf.space/--replicas/j9pup/")
result = client.predict(
		["https://images.news18.com/ibnlive/uploads/2016/06/Elon-Musk-Tesla.jpg", "https://cdn.businessinsider.de/wp-content/uploads/2019/06/elon-musk.jpg", "https://th.bing.com/th/id/OIP.iMIH_FCph8_sbye1RZx8kAHaFe?w=982&h=726&rs=1&pid=ImgDetMain"],	# List[filepath]  in 'Drag (Select) 1 or more photos of your face' File component
		"main img as an astronaut, profile picture, zoomed in, facing camera",	# str  in 'Prompt' Textbox component
		"bad quality, bad anatomy, worst quality, low quality, lowres, extra fingers, blur, blurry, ugly, wrong proportions, watermark, image artifacts, bad eyes",	# str  in 'Negative Prompt' Textbox component
		"Comic book",	# Literal['(No style)', 'Cinematic', 'Disney Charactor', 'Digital Art', 'Photographic (Default)', 'Fantasy art', 'Neonpunk', 'Enhance', 'Comic book', 'Lowpoly', 'Line art']  in 'Style template' Dropdown component
		60,	# float (numeric value between 20 and 100) in 'Number of sample steps' Slider component
		10,	# float (numeric value between 15 and 50) in 'Style strength (%)' Slider component
		1,	# float (numeric value between 1 and 4) in 'Number of output images' Slider component
		5,	# float (numeric value between 0.1 and 10.0) in 'Guidance scale' Slider component
		140609,	#float (numeric value between 0 and 2147483647) in 'Seed' Slider component
		api_name="/generate_image"
)
print(result)