# UmaKey

## 우마무스메 프리티 더비 for kakao with keyboard 프로젝트

##### 우마무스메 프리티 더비를 키보드로 즐기기

우마무스메 프리티 더비 for kakao를 PC환경에서 즐기는 사람이 많으나, 키보드에 대한 지원은 상대적으로 빈약하다.

기본적으로 1, 2, 3, 4, 5번과 ESC키를 사용 가능하지만, 이는 오직 훈련 선택 시에만 제한적으로 사용 가능하며, 사실상 키보드로 플레이하는 것은 불가능하다.

따라서 본 프로젝트에서는 우마무스메의 키보드 환경을 개선하는 것을 목표로 한다.

---

## 기능

핵심 기능은 다음과 같다.

1. 기초적인 키보드 매핑 기능
2. 필요에 따라 추가할 수 있는 매크로 기능
3. 키보드에 특정한 색상 매핑 기능

키보드 매핑은 당연히 지원한다. 특정 키를 누르면 해당 좌표를 클릭한다든지, 아니면 다른 키를 누른다든지 등의 기능을 구현할 수 있다.

매크로 기능은, 사용자가 원한다면 직접 매크로를 추가할 수 있다는 것이다. 현재 추가되어 있는 매크로 기능으로는, 트레이닝 화면에서 훈련 둘러보기 기능을 예시로 추가해 놨다.

그리고 색상 매핑 기능이 가장 핵심이다. 우마무스메 게임은 기본적으로 제한적인 색상의 UI를 가진 게임으로, 따라서 색상을 적절하게 추출하여 키보드에 할당해 놓는다면 하나의 키로 많은 동작을 수행할 수 있다.

예시로, 확인과 같은 버튼은 대부분 초록색, 취소 버튼은 흰색에 가까운 색상으로 통일되어 있다. 이러한 점을 고려할 때, 수많은 버튼을 하나씩 매핑하는 것보다 훨씬 효율적으로 다룰 수 있다. 

코드를 보면 알겠지만, 할당한 키는 다음과 같다.

    'Space': 초록버튼
    '`':     흰 버튼
    'Q':     휴식
    'W':     트레이닝
    'E':     스킬
    'R':     외출
    'F':     양호실
    'T':     레슨
    'G':     레이스
    'TAB':   훈련 돌아보기
    'A':     1번 선택지
    'S':     2번 선택지
    'D':     3번 선택지
    '/':     스킵버튼

아직 색상 추출과 처리 과정이 완벽하진 않다. 오작동할 수 있고, 인식하지 못할 수 있다. 그러나 한 번 사용해 보면, 훨씬 쾌적한 플레이를 즐길 수 있을 것이다.

### 사용법

1. 실행 시, 트레이 아이콘이 생성되며, 해당 아이콘을 통해 매핑 on/off, 게임 화면 정보 확인, 종료 기능을 수행할 수 있다.
2. 유저가 설정한 매핑에 따라 매핑을 추가하거나 제거할 수 있다. 이는 config.json 파일을 통해 조작할 수 있다.
3. 과도한 입력은 성능 저하를 불러올 수 있다. 또한, 색상 기반의 입력 수행 시 예상치 못한 결과를 초래할 수 있다.
4. 게임 화면을 벗어날 시 매핑은 해제되며, 프로그램을 종료하지 않을 시 게임 복귀 후 자동으로 매핑이 복구된다.
5. 좌표 기반의 매핑의 경우, 화면의 비율을 변경하지 않으면 화면 크기에 따라 자동으로 위치를 보정한다.

#### config 설정법

config 파일은 다음과 같은 구조이다.

```
{
    "key_mapping" : 
    {
        "Q": "[124, 203, 42]",
        "W": "[41, 122, 207]",
        "/": "(730, 1320)",
        "TAB": "Drag",
        ...
    },
    "Drag": "RIGHT_ARROW, sleep 0.1, RIGHT_ARROW, sleep 0.1, RIGHT_ARROW, sleep 0.1, RIGHT_ARROW"
}
```

매핑을 원하는 키를 좌측에, 원하는 색상, 좌표, 다른 키, 매크로 이름을 우측에 작성한다.

이 때, 규칙은 다음과 같다.

1. 색상     : 대괄호([]) 안에 작성한다. 총 3개의 정수를 입력하며, 각각 R, G, B에 대응한다.
2. 좌표     : 소괄호(()) 안에 작성한다. 총 2개의 정수를 입력하며, 각각 x, y좌표에 해당한다.
3. 키       : 총 1개의 키 이름을 입력한다.
4. 매크로   : 커스텀할 매크로의 이름을 입력한다.

이 때, 사용자는 프로그램의 Inspector 기능을 통해 게임 내 색상, 좌표를 파악할 수 있다.

지원하는 키는 config.json 파일에 수록되어 있다.

#### 매크로 작성법

config.json 파일의 key_mapping 밖에 지정해둔 매크로 이름을 좌측에, 원하는 기능을 우측에 작성한다. 이 때 각 명령은 (", ")로 구분한다.

Drag의 경우, 다음과 같이 실행된다.

우측 방향키 > 0.1초 딜레이 > 우측 방향키 > 0.1초 딜레이 > ...

key_mapping과 마찬가지로, 색깔을 입력하고 싶다면 대괄호 안에, 좌표를 입력하고 싶다면 소괄호 안에, 키를 입력하고 싶다면 키 이름을 입력한다.

매크로 속 매크로 역시 가능하다. 다음과 같은 매크로가 있다고 가정하자.

"MAC": "[0, 0, 0], (0, 0), ESC, sleep 1, MAC"

각각 RGB값이 0, 0, 0인 곳 클릭, 좌표 0, 0 클릭, ESC 누르기, 1초 쉬기, 그리고 다시 MAC 매크로를 호출한다. 

따라서 이 매크로는 무한 반복한다. (단, 이와 같은 형태는 권장하지 않는다.)

---

## update

    v0.0.2 : 성능 개선 마이너 업데이트
    v0.0.3 : 유저 설정 지원 추가, 게임 화면 정보 확인 기능 추가

    

### ***주의***

***반드시 관리자 권한으로 실행할 것. 아니면 키보드 입력을 받지 못한다.***

본 프로그램을 남용하여 발생하는 부작용은 책임지지 않음.

---

코드 실행 시 필요한 패키지

```
pip install pywin32 numpy opencv-python-headless Pillow pystray
```

---

## 목표

1. 색상 처리 부분 개선하기
