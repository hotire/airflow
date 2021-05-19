# Airflow
[airflow](https://github.com/apache/airflow)

[Apache Airflow](https://airflow.apache.org/)는 복잡한 계산을 요하는 작업흐름과 데이터 처리 파이프라인을 조율하기 위해 만든 오픈소스 도구이다. 

### Principles
- Scalable : 모듈 아키텍쳐이며 메시지큐를 사용하여 Worker 수를 조정한다. (분산구조와 메시지큐를 이용하여 많은 수의 워커간의 협업을 지원)
- Dynamic : Python으로 되어있고, 파이프 라인을 동적으로 생성하는 코드를 작성할 수 있다. 
- Extensible
- Elegant

### Pipeline

데이터 처리 단계의 출력이 다음 단계의 입력으로 이어지는 형태로 연결된 구조

### WMS

WMS 는 Workflow Management System 의 약자. Pipelining을 통해 목적을 달성하는 시스템

데이터를 옮기고 변경시켜서 어떤 작업을 수행하는 것으로, 예를들면 서버에서 로그를 수집해서 DB에 INSERT하는 작업

보통 크론잡을 통해 주기적으로 실행하다 문제가 발생하고 이를 관리하기 위해 사용한다. 


## Architecture

![architecture](/doc/img/arch-diag-basic.png)

- Scheduler
: 실행 주기가 되면 작업을 생성, 의존하는 작업이 모두 성공하면 Broker에 넘김

- Worker
: 실제 작업을 실행하는 주체

- Broker
:실행가능한 작업들이 들어가는 공간

- Meta DB
: DAG, Task 등이 정의되어있음
DAG run, Task Instance 관리


### Concepts
https://airflow.apache.org/docs/apache-airflow/stable/concepts.html#


사실 두가지만 알면 됩니다. DAG & Operator. DAG와 Operator를 결합하여 Task Instance를 만들면 복잡한 Workflow를 만들 수 있습니다.

- DAG : 작업이 수행되어야 하는 순서에 대한 설명
- Operator : 어떤 작업을 수행하기 위한 템플릿으로 작동하는 클래스
Task : Operator의 매개 변수화 된 인스턴스
Task Instance : 1) DAG에 할당되고 2) DAG의 특정 실행과 관련된 상태가 있는 Task


## Getting Started
https://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/
