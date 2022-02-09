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