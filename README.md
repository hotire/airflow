# airflow
[airflow](https://github.com/apache/airflow)

[Apache Airflow](https://airflow.apache.org/)는 복잡한 계산을 요하는 작업흐름과 데이터 처리 파이프라인을 조율하기 위해 만든 오픈소스 도구이다. 

### Principles
- Scalable : 모듈 아키텍쳐이며 메시지큐를 사용하여 Worker 수를 조정한다. (분산구조와 메시지큐를 이용하여 많은 수의 워커간의 협업을 지원)
- Dynamic : Python으로 되어있고, 파이프 라인을 동적으로 생성하는 코드를 작성할 수 있다. 
- Extensible
- Elegant


## Architecture

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


## Getting Started
https://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/
