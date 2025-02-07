python app/main.py --input input_video.mp4 --output output_video.mp4 --lang ar  
python app/main.py --input samples/my_video.mp4  
# إنشاء مجلد للمشروع
mkdir test-dubbing
cd test-dubbing

# تنزيل ملف فيديو تجريبي (مثال)
wget https://example.com/sample-video.mp4 -O input.mp4
# إنشاء ملف المتطلبات
echo "whisper-openai>=1.0
transformers>=4.30
ffmpeg-python>=0.2.0
torch>=2.0.0
mimic3>=1.0.0" > requirements.txt

# تثبيت الحزم
pip install -r requirements.txt

# تثبيت FFmpeg (لأنظمة Ubuntu/Debian)
sudo apt update && sudo apt install ffmpeg -y
# تشغيل البرنامج
python main.py
vlc output.mp4  # أو أي مشغل فيديو آخر
git commit -m "fix(audio): adjust sync delay in dubbed_audio.wav"
  git commit -m "docs: update installation guide in README.md"
 git add -p  # اختر التغييرات المرتبطة ببعضها
  git commit -m "feat(translation): add Arabic support using MarianMT"
 git checkout -b fix/indentation-errors  # إنشاء فرع للإصلاحات
  git checkout -b feat/add-french-translation  # فرع لميزة جديدة
  git rebase -i HEAD~5  # تعديل آخر 5 Commits
 git push origin main --force  # تحذير: استخدم --force بحذر!
 
