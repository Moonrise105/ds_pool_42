#!/bin/bash
curl -s -H "per_page=20&page=1" -X 'GET' "https://api.hh.ru/vacancies?text=${1// /%20}&per_page=20&page=0" | jq --raw-output '.' > hh.json
