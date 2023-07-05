from config import config
# TODO: Direction :: Pillow 라이브러리 불러오기
from PIL import Image


if __name__ == '__main__':
    # 대상 사진 파일 경로 불러오기
    file_path = config["file_path"] # 데스크톱에 있는 사진
    new_file_path = config["new_file_path"] # 데스크톱에 넣을 사진
    size = config["size"]

    # TODO: 이미지 열기
    img = Image.open(file_path)
    # TODO: 이미지 크기 조정
    resize_img = img.resize(size)
    # TODO: 이미지 저장
    resize_img.save(new_file_path)