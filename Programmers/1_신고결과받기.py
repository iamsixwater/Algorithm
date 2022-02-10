# 개선 코드
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reportee = {x: 0 for x in id_list}
    
    # k번 신고 당한 사람 색출
    for r in set(report):
        reportee[r.split()[1]] += 1
        
    # 신고자가 받을 메일 개수 도출
    for r in set(report):
        if reportee[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    
    return answer


# 기존 코드
'''
def solution(id_list, report, k):
    # (신고당한 사람, [신고한 사람 목록]) 생성
    report_string_set = set(report) # 중복 신고 제거
    report_set = dict()
    for str in report_string_set:
        reporter, reportee = str.split(" ")
        if reportee in report_set.keys():
            report_set[reportee].append(reporter)
        else:
            report_set[reportee] = [reporter]
    
    # 신고가 k번 미만인 사람 신고 목록에서 삭제
    for reportee in report_set.keys():
        if len(report_set[reportee]) < k:
            report_set[reportee] = []
        
    # 신고한 사람, 신고 성공 건 수
    report_success_dict = dict()
    for id in id_list:
        report_success_dict[id] = 0
    
    # 신고 성공한 사람 목록 확인
    for reporter_list in report_set.values():
        for reporter in reporter_list:
            report_success_dict[reporter] += 1
    
    print(report_success_dict)
    # report dict에서 value만 순서대로 추출: dict는 순서 보장 됨
    answer = []
    for reporter in report_success_dict:
        report_num = report_success_dict[reporter]
        answer.append(report_num)
    
    return answer
'''