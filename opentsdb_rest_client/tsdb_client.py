# -*- coding: utf-8 -*-
import time
import socket
import requests

class TsdbError(Exception):
    pass


def metric_point(metric, value, timestamp=None, tags=None):
    return dict(
        metric=metric,
        value=value,
        timestamp=timestamp or int(time.time()),
        tags=tags or dict(host=socket.gethostname())
    )

def query(aggregator, metric, tags=None, rate=False, rateOptions=None, downsample=None, filters=None, explicitTags=None, percentiles=None):
    return {k: v for k, v in dict(
        aggregator=aggregator,
        metric=metric,
        tags=tags,
        rate=rate,
        rateOptions=rateOptions,
        downsample=downsample,
        filters=filters,
        explicitTags=explicitTags,
        percentiles=percentiles
    ).items() if v is not None}  # remove None values


class Client(object):
    def __init__(self, api_url="http://127.0.0.1:4242/api", timeout=3):
        self.api_url = api_url
        self.timeout = timeout

    def _post_request(self, endpoint, json=None):
        try:
            response = requests.post(self.api_url + endpoint, json=json, timeout=self.timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as ex:
            raise TsdbError(ex.response.json()['error']['message'])
        except requests.exceptions.RequestException as ex:
            raise TsdbError(ex[0])

    def aggregators(self):
        return self._post_request("/aggregators").json()

    def config(self):
        return self._post_request("/config").json()

    def suggest(self, type, q=None, max=None):
        return self._post_request("/suggest", json=dict(
            type=type,
            q=q,
            max=max
        )).json()

    def query(self, queries, start="10m-ago", end=None):
        return self._post_request("/query", json=dict(
            start=start,
            end=end,
            queries=queries
        )).json()

    def put(self, payload):
        return self._post_request("/put", json=payload)

    def version(self):
        return self._post_request("/version").json()

    def dropcaches(self):
        return self._post_request("/dropcaches").json()

    def serializers(self):
        return self._post_request("/serializers").json()

    def stats(self):
        return self._post_request("/stats").json()

    def annotation(self):
        raise NotImplementedError()

    def rollup(self):
        raise NotImplementedError()

    def histogram(self):
        raise NotImplementedError()

    def search(self):
        raise NotImplementedError()

    def tree(self):
        raise NotImplementedError()

    def uid(self):
        raise NotImplementedError()
