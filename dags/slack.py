from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.slack_operator import SlackAPIPostOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'mskim',
    'depends_on_past': False,
    # 'start_date': airflow.utils.dates.days_ago(2),
}

with DAG(
    'test_slack',
    default_args=default_args,
    start_date=days_ago(2),
    schedule_interval='5 * * * *',
) as dag:

  t1 = SlackAPIPostOperator(
    task_id='send_slack',
    token='xoxb-token', 
    channel='channel',
    username='intern_daily_bot',
    text='Hi. I am from Airflow! \n'
  )

  t2 = BashOperator(
    task_id='print_date',
    bash_command='date',
    )
  t1 >> t2
