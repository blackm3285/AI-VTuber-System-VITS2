# AI-VTuber-System-VITS2
Replaced OpenAI TTS to local Bert-VITS2-2.3 Server

You can edit vits api prompt in ./TextToSpeech/OpenAITTS.py

```

......skip......

# Updated openaitts function using Gradio Client instead of OpenAI API
def openaitts(
        text="",
        output_path="Audio/output_openaitts_01.wav",
        model="tts-1",    # Kept in function signature, not used
        voice="alloy",    # Kept in function signature, not used
        speed=1.00,       # Kept in function signature, not used
        format="wav",     # Kept in function signature, not used
        timeout=10.0,     # Kept in function signature, not used
        speaker="Your_Speaker",    # Default speaker
        sdp_ratio=0.5,      # Default SDP Ratio
        noise_scale=0.5,    # Default Noise
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

......skip......

```

測試使用的VITS模型及執行端是來自以下"【AI东雪莲2.0（重制版）】在线语音合成" 的本地部屬版, 供各位參考
https://huggingface.co/spaces/XzJosh/Azuma-Bert-VITS2-2.3/tree/main

# How to install

1.下載原作者提供的1.3整合包

2.下載此處的 .\TextToSpeech\OpenAITTS.py

3.到下載好的 .\GUI_control_panel\runtime 裡開啟cmd執行 python -m pip install gradio==4.44.1

4.執行你的vits2客戶端 (app.py)

5.切換GUI裡的EdgeTTS到OpenAI TTS

6.完成
