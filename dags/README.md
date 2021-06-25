# DAGS

DAG(Directed Acyclic Graph, 비순환 방향 그래프)로 각 배치 스케쥴이 관리됩니다

DAG하위에는 고유한 여러 Task가 존재하며 순서를 갖습니다

Task는 BashOperator, PythonOperator 등 다양한 Operator를 지원합니다
