docker run -p 5000:5000 \
  -e SECRET_KEY='\xc3\x13\xe9%\xbdE]X\xb7Y\xdd\xea\xfeR9\x13' \
  -e RDS_HOST=ai-drawing-test.cdiulsaolpkv.ap-northeast-2.rds.amazonaws.com \
  -e RDS_PORT=3306 \
  -e RDS_USERNAME=admin \
  -e RDS_PASSWORD=flsfls852!! \
  -e RDS_DATABASE=ai_drawing_test \
  -e AWS_BUCKET_NAME='ai-drawing-test' \
  -e AWS_ACCESS_KEY_ID=AKIA5PGADPBNL565CYV3 \
  -e AWS_SECRET_ACCESS_KEY=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 \
  -e AWS_REGION=ap-northeast-2 \
  2299bc3f044f
