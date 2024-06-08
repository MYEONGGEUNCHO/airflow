from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_operator", # dag이름 -> airflow 화면에서 보이는 id
    schedule="0 0 * * *", # cron 스케쥴
    start_date=pendulum.datetime(2024, 6, 8, tz="Asia/Seoul"),  # locale
    catchup=False,   # false: 사이구간X true: 사이구간O, 한꺼번에 돌게됨;;
    # dagrun_timeout=datetime.timedelta(minutes=60), # 1시간 돌면 timeout
    # tags=["example", "example2"],
    params={"example_key": "example_value"},
) as dag:
    run_this_last = EmptyOperator(
        task_id="run_this_last",
    )

    # [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whomi",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    # task 도는 순서
    bash_t1 >> bash_t2