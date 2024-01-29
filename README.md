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
2. 필요에 따라 추가할 수 있는 메크로 기능
3. 키보드에 특정한 색상 매핑 기능

키보드 매핑은 당연히 지원한다. 특정 키를 누르면 해당 좌표를 클릭한다든지, 아니면 다른 키를 누른다든지 등의 기능을 구현할 수 있다.

메크로 기능은, 사용자가 원한다면 직접 메크롤르 추가할 수 있다는 것이다. 현재 추가되어 있는 메크로 기능으로는, 트레이닝 화면에서 훈련 둘러보기 기능을 예시로 추가해 놨다.

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
    'TAB':   훈련 돌아보기 // 주의 : 스피드가 활성화되어있으면 안된다. 그냥 1, 2, 3, 4, 5를 순서대로 눌러주는 기능.
    'A':     1번 선택지
    'S':     2번 선택지
    'D':     3번 선택지

아직 색상 추출과 처리 과정이 완벽하진 않다. 오작동할 수 있고, 인식하지 못할 수 있다. 그러나 한 번 사용해 보면, 훨씬 쾌적한 플레이를 즐길 수 있을 것이다.

### ***주의***

***반드시 관리자 권한으로 실행할 것. 아니면 키보드 입력을 받지 못한다.***

---

코드 실행 시 필요한 패키지

```
pip install pystray pillow pygetwindow opencv-python-headless numpy pywin32
```

코드 실행

```
python run.py
```

---

## 목표

1. 색상 처리 부분 개선하기
2. 더 많은 시나리오 지원하기 (현재 : 그랜드 라이브)
3. 좀 더 편한 설정기능 제작 (키보드 매핑, 메크로 제작 등)
