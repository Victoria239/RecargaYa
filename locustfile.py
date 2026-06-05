from locust import HttpUser, between, task


class RecargaYaUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def calcular_recarga(self):
        self.client.post(
            "/recargas/calcular",
            json={
                "monto": 30000,
                "premium": True,
            },
        )