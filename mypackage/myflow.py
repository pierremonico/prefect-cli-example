from prefect import Flow, task


@task
def hello_world():
    print("Hello Prefect!")


with Flow("Hello World") as flow:
    hello_world()

if __name__ == "__main__":
    flow.run()