from main import SEM

sem = SEM()

def test_find_excel():
	assert len(sem.file_paths) == 1

def test_get_data():
	assert len(sem.data[0]) == 6

def test_check_header():
	assert sem.check_header(['Search keyword','Impressions','CTR','Cost','Position','Company','Revenue']) == True
	assert sem.check_header(['keyword','Impressions','CTR','Cost','Position','Company','Revenue']) == False
