import shutil
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gradio_client import Client

# In TextToSpeech/OpenAITTS.py
OpenAITTS_Voice_list = ["Manual"]
OpenAITTS_Model_list = ["Manual"]

# Keeping the OpenAITTS parameter structure, though we will not use all parameters
openaitts_parameters = {
    "output_path":"Audio/output_openaitts_01.wav",
    "model":"tts-1",  # Not used in Gradio Client
    "voice":"alloy",  # Not used in Gradio Client
    "speed":1.00,     # Not used in Gradio Client
    "format":"wav",   # Not used in Gradio Client
    "timeout":10.0,   # Not used in Gradio Client
}


# Updated openaitts function using Gradio Client instead of OpenAI API
def openaitts(
        text="",
        output_path="Audio/output_openaitts_01.wav",
        model="tts-1",    # Kept in function signature, not used
        voice="alloy",    # Kept in function signature, not used
        speed=1.00,       # Kept in function signature, not used
        format="wav",     # Kept in function signature, not used
        timeout=10.0,     # Kept in function signature, not used
        speaker="Azuma",    # Default speaker
        sdp_ratio=0.9,      # Default SDP Ratio
        noise_scale=0.35,    # Default Noise
        noise_scale_w=0.9,  # Default Noise_W
        length_scale=1.0,   # Default Length scale
        language="auto",      # Default Language
        audio_prompt=None,          # Path for audio prompt (optional)
        text_prompt="",        # Default text prompt for style
        prompt_mode="Text prompt",  # Default prompt mode
        style_text="",      # Auxiliary text for style (optional)
        style_weight=0.7,   # Weight of the auxiliary text (optional)
        ):

    try:
        # Gradio Client initialization
        client = Client("http://127.0.0.1:7860/")
        
        # Calling the Gradio API with specific values
        result = client.predict(
            text,              # Input text for TTS
            speaker,           # Speaker selection
            sdp_ratio,         # SDP Ratio slider
            noise_scale,       # Noise slider
            noise_scale_w,     # Noise_W slider
            length_scale,      # Length scale slider
            language,          # Language dropdown
            audio_prompt,      # Audio prompt file path
            text_prompt,       # Text prompt for style
            prompt_mode,       # Prompt mode (Text/Audio)
            style_text,        # Auxiliary text for style
            style_weight,      # Weight of auxiliary text
            fn_index=0         # Function index for the correct Gradio function
        )
        print(result)

        # result is a tuple, and the second element contains the temp file path
        temp_file_path = result[1]  # Extracting the temp file path
        
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Copy the file from the temporary location to the output path
        shutil.copy(temp_file_path, output_path)

    except Exception as e:
        print(f"Error in Gradio TTS request: {e}\n")

# Main section to run the script
if __name__ == "__main__":

    input_text = "Never gonna give you up, never gonna let you down"
    
    openaitts(
        text=input_text,
        output_path="Audio/output_openaitts_01.wav",  # Still used for saving output
        model="tts-1",    # Unused in Gradio Client call
        voice="alloy",    # Unused in Gradio Client call
        speed=1.00,       # Unused in Gradio Client call
        format="wav",     # Unused in Gradio Client call
        timeout=10.0,     # Unused in Gradio Client call
    )