# 11-t2gether-backend Readme

# Introduction
* T2 - 호주 유명 Tea 브랜드의 웹사이트(t2tea.com)
* 개발기간 : 2020.08.18 ~ 2020.08.28(12일)
* 개발인원 : Front-end 4명(오승하, 강예지, 김규영, 마상원), Back-end 2명(이건규, 왕민욱)
* [Front-end Github](https://github.com/wecode-bootcamp-korea/11-t2gether-frontend)
* [Back-end Github](https://github.com/wecode-bootcamp-korea/11-t2gether-backend)

# Achivement
- 프론트엔드 사이드와의 소통을 경험해보고 보다 나은 협업이 될 수 있도록 노력
- 실질적으로 웹 서비스가 작동하는 방식을 구현
- 실무에서 사용하는 개발 방법론을 실제로 적용해보면서 익숙해지도록 노력 ex) 스크럼
- 많은 연관이 존재하는 데이터를 다루기 위한 모델링과 DB 운용을 경험


# Demo Video
[![Video Label](http://img.youtube.com/vi/_ENyBLFF7VU/0.jpg)](https://youtu.be/_ENyBLFF7VU)

# Modeling
![Imgur](https://i.imgur.com/IkH7lSt.png)

# Skill Stacks
* Python
* Django
* Bcrypt
* JWT
* MySQL
* CORS headers
* Git, Github
* AWS EC2, RDS
* Elasticsearch
* Scrapy

# Apps
* User
	- 유저정보 저장
  - 회원가입 / 로그인
  	- 유효성 검사
    - 패스워드 암호화
    - 로그인 시 JWT Access 토큰 발행
  - 로그인 상태인지 확인하는 데코레이터 함수
 
* Main
  - 웹 페이지에서 사용하는 이미지 전달
    - 메인 페이지
    - 페이지 Footer
   
* Product
  - 전체 상품 API
    - 전체 상품의 간략한 정보를 제공
  - 개별 상품 API
    - 개별 상품의 상세한 정보를 제공
	- 검색 기능
		- 제품 이름으로 검색 결과 반환
  - 데이터 필터링
		- 제품 태그를 통해서 필터링 구현

* Review
  - 개별 상품에 대한 리뷰 갯수
  - 개별 상품에 대한 별점 평균
  
# Settings
* AWS EC2 인스턴스 세팅
* AWS RDS MySQL 세팅
* unit test 진행
* github를 통한 프로젝트 버전 관리
* Elasticsearch를 사용한 검색 기능 위한 NoSQL DB 연결

# API Documentation
