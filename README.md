# 🎮유전 알고리즘을 이용한 끝나지 않는 테트리스
## 💜 프로젝트 진행 기간
- **기간**: 2023.09.08(월) ~ 2023.12.08(금) (92일간 진행)  
- **프로젝트**: 동의대 캡스톤 디자인 I
- **정기 회의**: 매주 1회, 2시간 (총 13주)
  - **총 회의 시간**: 26시간
- **개발 시간**: 매주 약 5시간
  - **총 개발 시간**: 약 65시간
  - 
## 목차
- [소개](#소개)
- [주요기술](#주요기술)
- [협업툴](#협업툴)
- [실행결과](#실행결과)
- [부록](#부록)

## 소개
이 프로젝트는 Pygame을 사용하여 테트리스를 구현하고, 유전 알고리즘을 이용하여 적절한 가중치를 탐색하여 테트리스 게임이 끝나지 않도록 하는 프로젝트입니다. 
유전 알고리즘을 통해 최적의 테트리스 블록 배치를 위한 가중치를 학습하여 무한히 지속되는 게임 플레이를 목표로 합니다.

## 주요기술
### Pygame
- **게임 개발 라이브러리**: Pygame은 파이썬을 위한 게임 개발 라이브러리로, 2D 게임 개발에 필요한 다양한 기능을 제공합니다.
- **이벤트 처리**: 키보드 및 마우스 이벤트를 처리하여 사용자 입력에 반응합니다.
- **그래픽 렌더링**: 텍스트를 화면에 렌더링합니다.

### 유전 알고리즘
- **진화적 접근법**: 유전 알고리즘은 자연 선택 과정을 모방하여 최적의 솔루션을 찾는 진화적 접근법입니다.
- **개체군(Population)**: 여러 솔루션(개체)을 생성하고, 이를 통해 문제를 해결합니다.
- **적합도 함수(Fitness Function)**: 각 개체의 성능을 평가하여 적합도를 계산합니다.
- **선택(Selection)**: 높은 적합도를 가진 개체들을 선택하여 다음 세대를 만듭니다.
- **교차(Crossover)**: 선택된 개체들을 결합하여 새로운 개체를 생성합니다.
- **돌연변이(Mutation)**: 새로운 개체에 약간의 변화를 주어 다양성을 증가시킵니다.
![1-30](https://github.com/user-attachments/assets/8f32a4c8-7b90-44f2-a16c-a2b179c2973d)

## 협업툴
- Git
  - 코드의 버전을 관리
  - 이슈 발행, 해결을 위한 토론
  - 코드리뷰를 진행하고 피드백 게시
- Notion
  - 회의가 있을때마다 회의록을 기록하여 보관
  - 기술확보 시, 다른 팀원들도 추후 따라할 수 있도록 보기 쉽게 작업 순서대로 정리
  - 기능명세서와 같은 모두가 공유해야 하는 문서 관리
  
## 실행결과 
![GIF](https://github.com/Sihyeon0123/Genetic-Algorithm-Tetris/assets/129951793/f054983e-b9c0-4080-91eb-278c4fcae982)

## 부록
- [기능명세서](./docs/캡스톤디자인I_기능요구사항명세서.xlsx)
- [계획서](./docs/캡스톤디자인I_계획서.hwp)
- [결과보고서](./docs/캡스톤디자인I_결과보고서.hwp)
- [최종발표자료](./docs/캡스톤디자인_발표자료.pptx)
