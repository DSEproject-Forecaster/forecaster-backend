from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    @task(1)
    def daily_seasonality(self):
        self.client.get('http://localhost:5050/dashboard/getDailySeasonalData/')

    @task(2)
    def yearly_seasonality(self):
        self.client.get('http://localhost:5050/dashboard/getYearlySeasonalData/')
        
    @task(3)
    def trends(self):
        self.client.get('http://localhost:5050/dashboard/getTrends/')

    @task(4)
    def correlations(self):
        self.client.get('http://localhost:5050/dashboard/getCorrelations/')

    @task(5)
    def box_plots(self):
        self.client.get('http://localhost:5050/dashboard/getBoxPlots/')

    @task(6)
    def radar(self):
        self.client.get('http://localhost:5050/dashboard/getRadar/?year=2020')