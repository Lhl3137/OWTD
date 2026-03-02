from perception_module import detect_oilwells
from scene_understanding import get_initial_description
from risk_assessment import generate_final_report

def main():
    image_path = "" # 输入图片路径
    
    print("目标提取")
    oilwell_detections = detect_oilwells(image_path)
    print(f"检测到 {len(oilwell_detections)} 个油井")
    
    print("提取图像全局语义信息")
    initial_description = get_initial_description(image_path)
    
    print("生成安全评估报告")
    final_report = generate_final_report(oilwell_detections, initial_description)
    
    with open("analysis_report.html", "w", encoding="utf-8") as f:
        f.write(final_report)
    print("安全评估报告已保存到 analysis_report.html")

if __name__ == "__main__":
    main() 