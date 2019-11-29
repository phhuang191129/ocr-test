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
            if '病名' in txt or '診斷' in txt or '名' in txt and '姓名' not in txt:
                diseaseStart = i+1
            if '醫師囑言' in txt or '醫囑' in txt or '病患' in txt :
                diseaseEnd = i
                break
        if diseaseStart and diseaseEnd:
            for i in range(diseaseStart,diseaseEnd):
                disease['disease']+= self.result[i][1]
        self.res.update(disease)


    def disposalConsideration(self):
        """
        醫囑
        """
       
        disposalConsideration = {'disposalConsideration': ''}
        disposalConsiderationStart = disposalConsiderationEnd = None
        for i in range(self.N):
            txt = self.result[i][1].replace(' ','')
            
            if '醫師囑言' in txt or '醫囑' in txt or '嘱言' in txt:
                disposalConsiderationStart = i+1
            if '病患' in txt and not disposalConsiderationStart:
                disposalConsiderationStart = i
             
            if '以下空白' in txt :
                disposalConsiderationEnd = i+1
                
            if '以上病人' in txt or '立日期' in txt and not disposalConsiderationEnd:
                disposalConsiderationEnd = i
       
                break
            
        if disposalConsiderationStart and disposalConsiderationEnd:
            for i in range(disposalConsiderationStart,disposalConsiderationEnd):
                disposalConsideration['disposalConsideration'] += self.result[i][1]
            disposalConsideration['disposalConsideration'] = disposalConsideration['disposalConsideration'].split('以下空白')[0]
        self.res.update(disposalConsideration)
  

