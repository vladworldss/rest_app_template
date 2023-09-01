#!/bin/bash
#Запуск функциональных тестов локально
docker-compose -f docker-compose.yml -f docker-compose.local.yml up -V --exit-code-from tests tests
