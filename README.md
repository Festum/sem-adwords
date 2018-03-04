# Python Engineer - Marketing Technology: Take-Home Test

---

## Getting start

Install:

```
git clone
cd sem-adwords
virtualenv venv
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

Run: `python main.py`
Run test: `pytest`


## Q&A

### Metrics

- [Impressions](https://support.google.com/adwords/answer/6320?hl=en)
An impression is counted each time ad is shown on search result

- CTR
`( No. of Clicks / No. of Impressions ) * 100`
Having high CTR leads to high QS, that results in lower CPC and good ad positions.

- [Position](https://support.google.com/adwords/answer/1722122?hl=en)
Ad position is the order in ad shows up on a page. Lower value means higher visibility.

- Cost/Revenue
Basic finance I/O values

- CPM
`Cost/Impressions*1000`

- **SEMP**
`(impressions * cost * position) / (ctr * revenue)`
Lower value means more profit efficient. Revenue ratio is revenue divide impressions and cost.

- Need to improve
Shows TOP 5 highest position keywords

### What are the recommendations

Put more attention on lower position keywords like `["tourist information milan", "montjuic castle entrance fee", "louis armstrong park", "mallorca tour guides", "lyon city tour"]`


### The pros and cons

- Pros

Knowing the basic profit assumption and keywords needed to improve

- Cons

Not efficiently merge these keywords. Should have time and other parameters to get a more precise assumption.
