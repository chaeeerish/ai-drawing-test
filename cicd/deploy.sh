#!/bin/bash

# 변수 설정
DOCKER_APP_NAME="ai-drawing-test"

# 체크할 컨테이너 이름 설정
BLUE_BACKEND_CONTAINER="${DOCKER_APP_NAME}-blue-backend-1"
BLUE_FRONTEND_CONTAINER="${DOCKER_APP_NAME}-blue-frontend-1"

GREEN_BACKEND_CONTAINER="${DOCKER_APP_NAME}-green-backend-1"
GREEN_FRONTEND_CONTAINER="${DOCKER_APP_NAME}-green-frontend-1"


# 컨테이너 스위칭
if ! docker ps -f name=${BLUE_BACKEND_CONTAINER} -f name=${BLUE_FRONTEND_CONTAINER} --format "{{.Names}}" | grep -qE "${BLUE_BACKEND_CONTAINER}|${BLUE_FRONTEND_CONTAINER}"; then
    echo "blue up"
    docker-compose -p ${DOCKER_APP_NAME}-blue -f /home/ubuntu/docker-compose.blue.yaml up -d
    BEFORE_COMPOSE_COLOR="green"
    AFTER_COMPOSE_COLOR="blue"
else
    echo "green up"
    docker-compose -p ${DOCKER_APP_NAME}-green -f /home/ubuntu/docker-compose.green.yaml up -d
    BEFORE_COMPOSE_COLOR="blue"
    AFTER_COMPOSE_COLOR="green"
fi
sleep 10

# 새로운 컨테이너가 제대로 떴는지 확인
if docker inspect ${DOCKER_APP_NAME}-${AFTER_COMPOSE_COLOR}-backend-1 >/dev/null 2>&1 && docker inspect ${DOCKER_APP_NAME}-${AFTER_COMPOSE_COLOR}-frontend-1 >/dev/null 2>&1; then
    # nginx.config를 컨테이너에 맞게 변경해주고 reload 한다
    sudo -S cp /etc/nginx/nginx.${AFTER_COMPOSE_COLOR}.conf /etc/nginx/nginx.conf
    nginx -s reload

    # 이전 컨테이너 종료
    if docker ps -q -f name="${DOCKER_APP_NAME}-${BEFORE_COMPOSE_COLOR}-backend-1" >/dev/null; then
        echo "${BEFORE_COMPOSE_COLOR} 이전 컨테이너(BE)가 실행 중입니다. 컨테이너를 중지합니다."
        docker stop ${DOCKER_APP_NAME}-${BEFORE_COMPOSE_COLOR}-backend-1
        docker rm -f ${DOCKER_APP_NAME}-${BEFORE_COMPOSE_COLOR}-backend-1
    fi
    if docker ps -q -f name="${DOCKER_APP_NAME}-${BEFORE_COMPOSE_COLOR}-frontend-1" >/dev/null; then 
        echo "${BEFORE_COMPOSE_COLOR} 이전 컨테이너(FE)가 실행 중입니다. 컨테이너를 중지합니다."
        docker stop ${DOCKER_APP_NAME}-${BEFORE_COMPOSE_COLOR}-frontend-1
        docker rm -f ${DOCKER_APP_NAME}-${BEFORE_COMPOSE_COLOR}-frontend-1
    fi

    echo "$BEFORE_COMPOSE_COLOR down"
fi

# 초기화
docker image prune