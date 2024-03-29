# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:59:48 2019

@author: matan
"""

import os
import pandas as pd
import numpy as np

os.chdir('C:/Users/matan/law')

rawdfHaifa = pd.read_excel('Haifa.xlsx')

dfHaifa = rawdfHaifa.copy()

nonTranslatedColumns = list(rawdfHaifa.columns)

translatedColumns = ['TrialCaseArea',
                   'TrialCaseSerial',
                   'TrialCaseName',
                   'TrialCaseNum',
                   'TrialCourt',
                   'AttorneyUnit',
                   'CaseDateOpened',
                   'CaseType1',
                   'CaseType2',
                   'CaseType3',
                   'PlaintiffRepresentative',
                   'Plaintiff',
                   'PlaintiffBirthDay',
                   'DateEvent',
                   'SumAskedCalculatedPlaintiff',
                   'SumAskedSpecial',
                   'SumAskedTotal',
                   'SumAskedSource',
                   'SumAskedCalculatedDefendant',
                   'WageBaseCalculations',
                   'VedictDisabilityPercentage',
                   'DefendantGov1',
                   'DefendantGov2',
                   'DefendantGov3',
                   'DefendantGov4',
                   'DefendantNontGov1',
                   'DefendantNontGov2',
                   'DefendantNontGov3',
                   'GovIfRepImmunity',
                   'GovisPrimaryDefendant',
                   'GovGuiltResponsibility',
                   'GovGuiltClaimsPercentage',
                   'GovGuiltClaims',
                   'GovGuiltClaimsAccepted',
                   'GovSideCStatement',
                   'GovCausalStatement',
                   'ExpertProsecutor5Name',
                   'ExpertProsecutor5Field',
                   'ExpertProsecutor5Percent',
                   'ExpertProsecutor5Remarks',
                   'ExpertProsecutor4Name',
                   'ExpertProsecutor4Field',
                   'ExpertProsecutor4Percent',
                   'ExpertProsecutor4Remarks',
                   'ExpertProsecutor3Name',
                   'ExpertProsecutor3Field',
                   'ExpertProsecutor3Percent',
                   'ExpertProsecutor3Remarks',
                   'ExpertProsecutor2Name',
                   'ExpertProsecutor2Field',
                   'ExpertProsecutor2Percent',
                   'ExpertProsecutor2Remarks',
                   'ExpertProsecutor1Name',
                   'ExpertProsecutor1Field',
                   'ExpertProsecutor1Percent',
                   'ExpertProsecutor1Remarks',
                   'ExpertDefendant4Name',
                   'ExpertDefendant4Field',
                   'ExpertDefendant4Percent',
                   'ExpertDefendant4Remarks',
                   'ExpertDefendant3Name',
                   'ExpertDefendant3Field',
                   'ExpertDefendant3Percent',
                   'ExpertDefendant3Remarks',
                   'ExpertDefendant2Name',
                   'ExpertDefendant2Field',
                   'ExpertDefendant2Percent',
                   'ExpertDefendant2Remarks',
                   'ExpertDefendant1Name',
                   'ExpertDefendant1Field',
                   'ExpertDefendant1Percent',
                   'ExpertDefendant1Remarks',
                   'ExpertCourt1Name',
                   'ExpertCourt1Field',
                   'ExpertCourt1Percent',
                   'ExpertCourt1Remarks',
                   'ExpertCourt2Name',
                   'ExpertCourt2Field',
                   'ExpertCourt2Percent',
                   'ExpertCourt2Remarks',
                   'ExpertCourt3Name',
                   'ExpertCourt3Field',
                   'ExpertCourt3Percent',
                   'ExpertCourt3Remarks',
                   'VedictReason',
                   'VerdictDate',
                   'VedictClaims',
                   'VerdictCourtCausal,'
                   'VerdictSumReceived',
                   'VerdictSumGov',
                   'VerdictType',
                   'VerdictSum',
                   'VedictFactors01',
                   'VedictFactors02',
                   'VedictFactors03',
                   'VedictFactors04',
                   'VedictFactors05',
                   'VedictFactors06',
                   'VedictFactors07',
                   'VedictFactors08',
                   'VedictFactors09',
                   'VedictFactors10',
                   'VedictFactors11',
                   'VedictFactors12',
                   'VedictFactors13',
                   'VedictFactorsOther',
                   'AppealCourt',
                   'AppealFileNum',
                   'AppealWho',
                   'AppealVerdict',
                   'AppealDate',
                   'AppealClaims',
                   'AppealSum',
                   'AppealStateGov',
                   'AppealFactors01',
                   'AppealFactors02',
                   'AppealFactors03',
                   'AppealFactors04',
                   'AppealFactors05',
                   'AppealFactors06',
                   'AppealFactors07',
                   'AppealFactors08',
                   'AppealFactors09',
                   'AppealFactors10',
                   'AppealFactors11',
                   'AppealFactorsOther']