from typing import TypedDict

IAssessment = TypedDict("IAssessment", {'indicator': str, 'user': str, 'demoSite': str, 'value': float, 'reference_value': float, 
                                        'min_value': float, 'max_value': float, 'is_inverse': bool, 'alternative_description': str, 
                                        'normalized_value': float, 'stakeHolderType': str, 'degreeOfCertainty': float})