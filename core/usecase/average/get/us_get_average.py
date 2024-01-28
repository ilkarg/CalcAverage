from rest_framework.response import Response
from modules.module_average.orm.model.average.requests.request_get_all_average import RequestGetAllAverage
import datetime
import pandas as pd
import json

class UsGetAverage:
    def execute(request):
        data = RequestGetAllAverage.execute()
        for obj in data:
            obj['time'] = datetime.datetime.fromisoformat(obj['time'])
            obj['average_value'] = float(obj['average_value'])

        df = pd.DataFrame(data)
        df['time'] = pd.to_datetime(df['time'])

        df_grouped = df.groupby(pd.Grouper(key='time', freq='10min'))
        response = df_grouped['average_value'].mean().reset_index().to_dict(orient='records')

        return Response(response)