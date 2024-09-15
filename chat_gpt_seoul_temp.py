import csv

# 파일 경로 설정
file_path = 'C:/Users/User/Downloads/seoul_temp.csv'

# 변수 초기화
max_temp = -float('inf')  # 가장 높은 온도를 저장하기 위한 변수
max_temp_date = ''        # 가장 높은 온도가 발생한 날짜를 저장하기 위한 변수

# CSV 파일 읽기
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # 첫 번째 줄은 헤더 (열 이름)

    # 'date'와 'max_temp'에 해당하는 인덱스 찾기
    date_index = header.index('date')
    max_temp_index = header.index('max_temp')

    # 각 행을 순회하며 최고 기온 찾기
    for row in reader:
        try:
            temp = float(row[max_temp_index])
            if temp > max_temp:
                max_temp = temp
                max_temp_date = row[date_index]
        except ValueError:
            # 온도가 숫자가 아닌 경우 건너뜀
            continue

# 결과 출력
print(f"서울의 온도가 가장 높은 날: {max_temp_date}, 온도: {max_temp}°C")
