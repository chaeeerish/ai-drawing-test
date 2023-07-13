FROM python:3.7.12

# 필요한 파일을 이미지로 복사
COPY main/ /app/main/
COPY ml_models/ /app/ml_models/
COPY app.py /app/
COPY requirements.txt /app/

# 작업 디렉토리 설정
WORKDIR /app

RUN pip install --upgrade pip==23.1.2
RUN pip install -r requirements.txt 
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN pip3 install tensorflow
RUN pip install gunicorn

# Nvidia Docker 저장소 추가
RUN distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
    && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | apt-key add - \
    && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | tee /etc/apt/sources.list.d/nvidia-docker.list \
    && apt-get update

# Nvidia Docker 설치
RUN apt-get install -y nvidia-docker2

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
