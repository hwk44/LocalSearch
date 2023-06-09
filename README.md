# LocalSearch
> First-Choice 알고리즘 => TSP => 시각화
> <br> Steepest => 경사하강법 => 수식(함수) 의 극대 / 극소 => 시각화


<hr>

## Search (Global)
    
### Local Search
    TSP, N-Queen(그래프) => 정답이 있음
        => X 경사하강법 (경사가 없음)
        => 유전 알고리즘

    수식 => 적절한 답을 제시
        => 언덕 알고리즘
        
        

### 검색알고리즘
    검색은 대부분 정렬을 동반함.
    정렬은 메모리를 필요로 함
    메모리를 적게 쓰는 데에 집중

    이진 검색(가장 대표적)
    정렬을 동반하지 않는 검색문제 N.P(대표적) => Local
    제한된 조건(Local) 하에서 풀림 => 조건을 어떻게 설정할 것인가?

<hr>

### 코딩 테스트 관련
    1. 그래프 문제 => 트리를 해결
    2. 트리 문제 => 트리로 해결 (재귀 자바는 재귀(X),
                                  파이썬,C, C++(꼬리재귀 지원))
    3. 정렬 관련X => 검색 문제
    4. 기본자료구조는 반드시 언어에서 제공하는 걸 사용한다

<hr>

### foreach ... => 반복문[
    generator async await

### Hill Climb Algorithm
    특정 좌표(x,y)를 기준으로 가장 낮/높은 값을 찾아라
    좌표를 기반으로 좌우 값을 좀 더 살펴보자 => 계산이 오래 걸림
    
    언덕 등반 => 지역
    First => 지역(전역) => O.K = > 계산이 너무 느림
    Gradient Descent => 계산(뺄셈)이 빠름 (TSP) => 수식

### TSP 
    1) 어디서 시작할것인가? => 시작지점은 랜덤을 사용한다.
        -> 랜덤을 사용해 그나마 값이 적정값이라 가정하는 것

    2) first_choice, 좌우를 둘러봐라
        -> 지역 최적을 검색해야하는데
        -> 해당 코드는 전역 최적을 찾는 알고리즘임
<hr>

#### TSP 시각화
> TSP 관련 알고리즘을 시각적으로 확인할 수 있는 방법을 제시
>     
    거리계산 => 맨해튼, 유클리드 거리 => 테이블로 만듦
    최단거리 계산 => 최적인지는 확신할수 없음


##### 첫번째 도전
    - 목표 : 일단 뭐라도 화면에 나와라
        - 설정
        - 화면에 뭐라도 나오게
    - 격자로 뭐가 나오던가, 아니면 옆으로 길게 나왔으면 좋겠다.
    - 선이랑 점이 그려져야 함
        - 
##### 두번째 도전
    - 목표 : TSP 문제를 만들어서 화면에 출력
    - TSP 문제를 어떻게 만드나요? 
        - (좌표) 냅다 30개 만들면 되지 않을까?>
        - 30개 겹치면 어쩌나?
    - 선이랑 점이 그려져야 함
        - TSP 문제가 있어야 선을 그리든 점을 그리든..
    - 알고리즘
        - BF 브루트 포스
    
<hr>

#### First Choice
    언덕등반, 전역검색
    Mutation(임의의 자료, Noise)

<hr>

### 공부해야할거
    random(uniform) eval exec
    pytest / junit => 켄트백 "테스트 주도 개발"


### 상태와 메서드
    메서드 : 상태를 변경하는 방법 / 계약
    상태 : 메모리에 위치한 객체의 현재 속성 값/ 참조 가능

## Local Search (언덕 등반)
    TSP, N-Queen => 좌표 => 조합론
    수식(방정식) => 경사하강법(미분)
    확률적 경사하강법 (미분)