import os
import shutil
import sys

# Windows에서 UnicodeEncodeError 방지를 위해 출력 인코딩을 UTF-8로 설정
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def classify_files():
    """
    지정된 폴더의 파일들을 확장자에 따라 분류하여
    바탕화면의 특정 폴더로 이동합니다.
    """
    # 소스 폴더와 바탕화면 경로 설정
    # r'' 형태는 경로에 있는 백슬래시(\)를 문자로 인식하게 해줍니다.
    source_folder = r'C:\Users\bjh49\OneDrive\문서\카카오톡 받은 파일'
    desktop_path = r'C:\Users\bjh49\OneDrive\바탕 화면'

    # 분류 규칙 정의 (폴더명: [확장자들])
    categories = {
        '사진': ['.jpg', '.jpeg', '.png', '.gif'],
        '문서': ['.pdf', '.docx', '.xlsx', '.hwp', '.pptx', '.txt'],
        '영상': ['.mp4', '.mov', '.avi'],
        '압축': ['.zip']
    }

    # 카테고리별 대상 폴더 경로 생성
    dest_paths = {
        category: os.path.join(desktop_path, category)
        for category in categories.keys()
    }

    # 대상 폴더가 없으면 생성
    for path in dest_paths.values():
        os.makedirs(path, exist_ok=True)

    # 소스 폴더가 존재하는지 확인
    if not os.path.isdir(source_folder):
        print(f"오류: 소스 폴더 '{source_folder}'를 찾을 수 없습니다.")
        return

    print(f"'{source_folder}'의 파일 정리를 시작합니다...")

    # 소스 폴더의 모든 파일에 대해 반복
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)

        # 파일인 경우에만 처리
        if os.path.isfile(source_file):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            # 어떤 카테고리에 속하는지 확인
            for category, extensions in categories.items():
                if file_ext in extensions:
                    dest_folder = dest_paths[category]
                    try:
                        # 파일 이동
                        shutil.move(source_file, os.path.join(dest_folder, filename))
                        print(f"  - '{filename}' -> '{category}' 폴더로 이동했습니다.")
                        moved = True
                        break
                    except Exception as e:
                        print(f"  - '{filename}' 이동 중 오류 발생: {e}")
                        moved = True # 오류가 발생해도 다른 카테고리로 재시도하지 않음
                        break
            
            if not moved:
                print(f"  - '{filename}'은(는) 분류되지 않았습니다.")

    print("\n파일 정리가 완료되었습니다.")

# 스크립트 실행
if __name__ == "__main__":
    classify_files()
