#!/usr/bin/env python3

import sys
import glob, os
import csv
import logging
import json
from statistics import mean

class SEM:
    """Parse data from Excel and make some calculation"""
    file_paths = []
    # logging.basicConfig(format=FORMAT
    data = []

    def __init__(self):
        self.find_excel()
        self.get_data()

    def find_excel(self, folder_path=os.path.dirname(os.path.realpath(__file__))):
        os.chdir(folder_path)
        for f in glob.glob("*.csv"):
            self.file_paths.append(f)

    def get_data(self):
        for file_path in self.file_paths:
            with open(file_path) as f:
                reader = csv.reader(f)
                if not self.check_header(next(reader)):
                    logging.warning('CSV file {} format might incorrect'.format(file_path))
                    break
                data = {}
                for row in reader:
                    company = row[5]
                    if company not in data:
                        data[company] = []
                    data[company].append({
                        'keyword': row[0],
                        'impressions': float(row[1]),
                        'ctr': float(row[2]),
                        'cost': float(row[3]),
                        'rank': float(row[4]),
                        'position': float(row[6]),
                        'revenue': float(row[6]),
                        'cpm': float(row[3])/float(row[3])*1000 if float(row[3])>0 else 0
                    })
                self.data.append(data)

    def check_header(self, header):
        return ['Search keyword','Impressions','CTR','Cost','Position','Company','Revenue'] == header

    def calc(self):
        for d in self.data:
            result = []
            for company, history in d.items():
                semp, l = self.company_sem(history)
                result.append({
                    'company': company,
                    'semp': semp,
                    'need_to_improve': l,
                })

            result = json.dumps(sorted(result, key=lambda x: x['semp']))
            print result

    def keyword_sem(self, k):
        return (k['impressions'] * k['cost'] *k['rank'])/(k['ctr'] * k['revenue'])

    def need_improve(self, obj):
        pos_list = sorted([{'position': v['position'],'keyword': k} for k, v in obj.iteritems()], key=lambda x: x['position'])
        keywords = []
        return [v['keyword'] for v in pos_list][:5]

    def company_sem(self, keywords):
        sem_by_keyword = {}
        for k in keywords:
            sem = self.keyword_sem(k)
            position = k['position']
            if k['keyword'] in sem_by_keyword:
                sem = sem+sem_by_keyword[k['keyword']]['sem']
                position = (position + sem_by_keyword[k['keyword']]['position'])/2

            sem_by_keyword[k['keyword']] = {'sem': sem , 'position': position}

        return mean([v['sem'] for k, v in sem_by_keyword.iteritems()]), self.need_improve(sem_by_keyword)

if __name__ == "__main__":
    sem = SEM()
    sem.calc()
