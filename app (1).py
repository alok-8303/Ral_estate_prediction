import gradio as gr
import numpy as np
import pickle

# Load the model
model = pickle.load(open('model.sav', 'rb'))

# Define the prediction function
def predict_price(Distance_to_the_nearest_MRT_station, Number_of_convenience_stores, Latitude, Longitude):
    inputs = [[Distance_to_the_nearest_MRT_station, Number_of_convenience_stores, Latitude, Longitude]]
    result = model.predict(inputs)
    updated_res = result.flatten().astype(float)
    return f'The predicted House Price per unit area is ${updated_res[0]:.2f}'

# Define the input components and launch the Gradio interface
# Updated: Use gr.Slider instead of gr.inputs.Slider
# Updated: Use gr.Textbox instead of gr.outputs.Textbox
iface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Slider(0.0, 10000.0, label="Distance to the Nearest MRT Station (meters)"),
        gr.Slider(0, 340, label="Number of Convenience Stores"),
        gr.Slider(-90.0, 90.0, label="Latitude"),
        gr.Slider(-180.0, 180.0, label="Longitude"),
    ],
    outputs=gr.Textbox(label="Predicted House Price per Unit Area"),
    title="Real Estate Price Predictor",
    description="Drop in the required Inputs, and we will do the rest."
)

# Launch the app
iface.launch()
