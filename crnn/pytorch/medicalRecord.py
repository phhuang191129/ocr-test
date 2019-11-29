import re

class case:
    """
    病例結構化輸出
    """
    def __init__(self,result):
        self.result = result
        self.N = len(self.result)
        self.res = {}
        self.disease()
        self.disposalConsideration()

    def disease(self):
        """
        病名、診斷
        """
        disease = {'disease':''}
        diseaseStart = diseaseEnd = None
        for i in range(self.N):
            txt = self.result[i][1].replace(' ','')
            if '病名' or '診斷' in txt :
                diseaseStart = i
            if '醫師囑言' or '醫囑' in txt :
                diseaseEnd = i
                break
        if diseaseStart and diseaseEnd:
            for i in range(diseaseStart,diseaseEnd):
                disease['disease'].join(self.result[i][1])
        self.res.update(disease)


    def disposalConsideration(self):
        """
        醫囑
        """
        disposalConsideration = {'disposalConsideration': ''}
        disposalConsiderationStart = disposalConsiderationEnd = None
        for i in range(self.N):
            txt = self.result[i][1].replace(' ','')
            if '醫師囑言' or '醫囑' in txt:
                disposalConsiderationStart = i+1
            if '以下空白' in txt :
                disposalConsiderationEnd = i+1
        if disposalConsiderationStart and disposalConsiderationEnd:
            for i in range(disposalConsiderationStart,disposalConsiderationEnd):
                disposalConsideration['disposalConsideration'].join(self.result[i][1])
        self.res.update(disposalConsideration)

