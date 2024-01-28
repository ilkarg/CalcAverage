from modules.module_average.orm.model.average.average import Average

class RequestGetAllAverage:
    def execute():
        return Average.objects.values()