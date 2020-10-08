def main():
    print("오늘은 평균값에 대해서 계산해보겠습니다")
    print("평균은 각 숫자를 더한 후에 그것을 각 숫자의 갯수로 나눈 값입니다.")

    score1, score2 = map(int, input("정수 두 숫자 입력해 보세요: ").split(","))
    
    print("이것이 평균입니다", (score1+score2)/2)

main()