import whisper
from transformers import MarianMTModel, MarianTokenizer
import subprocess
import ffmpeg

def transcribe_video(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    return result["text"]

def translate_text(text, target_lang="ar"):
    model_name = f"Helsinki-NLP/opus-mt-en-{target_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    translated = model.generate(**tokenizer(text, return_tensors="pt"))
    return tokenizer.decode(translated[0], skip_special_tokens=True)

def generate_audio(text, output_path="dubbed_audio.wav"):
    subprocess.run(f"mimic3 --voice ar_JO '{text}' --output {output_path}", shell=True)

def merge_audio_video(video_path, audio_path, output_path="output.mp4"):
    (
        ffmpeg
        .input(video_path)
        .output(output_path, vcodec='copy', acodec='aac', strict='experimental')
        .overwrite_output()
        .run()
    )

if __name__ == "__main__":
    # الخطوة 1: تحويل الصوت إلى نص
    original_text = transcribe_video("input.mp4")
    print(f"النص الأصلي: {original_text}")

    # الخطوة 2: الترجمة
    translated_text = translate_text(original_text, "ar")
    print(f"النص المترجم: {translated_text}")

    # الخطوة 3: توليد الصوت
    generate_audio(translated_text, "dubbed.wav")

    # الخطوة 4: دمج الصوت مع الفيديو
    merge_audio_video("input.mp4", "dubbed.wav", "output.mp4")
    print("تم الإنتهاء! الفيديو الجديد: output.mp4")import whisper  
from transformers import MarianMTModel, MarianTokenizer  
import ffmpeg  
import subprocess  
import os  

# --- استخراج النص من الفيديو ---  
def transcribe_video(video_path):  
    model = whisper.load_model("base")  
    result = model.transcribe(video_path)  
    return result["text"]  

# --- ترجمة النص ---  
def translate_text(text, target_lang="ar"):  
    model_name = f"Helsinki-NLP/opus-mt-en-{target_lang}"  
    tokenizer = MarianTokenizer.from_pretrained(model_name)  
    model = MarianMTModel.from_pretrained(model_name)  
    translated = model.generate(**tokenizer(text, return_tensors="pt"))  
    return tokenizer.decode(translated[0], skip_special_tokens=True)  

# --- توليد الصوت من النص المترجم ---  
def generate_audio(text, output_path="dubbed_audio.wav"):  
    subprocess.run(f"mimic3 --voice ar_JO '{text}' --output-dir {output_path}", shell=True)  

# --- دمج الصوت مع الفيديو ---  
def merge_audio_video(video_path, audio_path, output_path="output.mp4"):  
    (  
        ffmpeg  
        .input(video_path)  
        .output(output_path, vcodec='copy', acodec='aac', strict='experimental')  
        .overwrite_output()  
        .run()  
    )  

# --- الدالة الرئيسية ---  
if __name__ == "__main__":  
    # 1. استخراج النص  
    original_text = transcribe_video("input_video.mp4")  
    # 2. ترجمة النص  
    translated_text = translate_text(original_text, target_lang="ar")  
    # 3. توليد الصوت  
    generate_audio(translated_text, "dubbed_audio.wav")  
    # 4. دمج مع الفيديو  
    merge_audio_video("input_video.mp4", "dubbed_audio.wav", "output_video.mp4")  
    print("تمت الدبلجة بنجاح! 🎉")  
