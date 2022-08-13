class Solution:
    def isValid(self, s: str) -> bool:
        # 괄호별 열기 - 닫기 dict 생성
        pmap = {"(": ")", "{": "}", "[": "]"}
        
        _s_check = []
        for _s in s:
            if _s in ("(", "{", "["):
                # 시작 괄호 추가
                _s_check.append(_s)
            elif not _s_check:
                # 처음이 시작 괄호가 아닌 경우
                return False
            else:
                # 괄호가 올바르게 맵핑되었는지 확인
                if pmap[_s_check.pop()] != _s:
                    return False
        if _s_check:
            # for loop 끝나면 _s_check가 비어있어야 하는데 아닌 경우 (닫기 괄호가 없던 경우)
            return False
        return True