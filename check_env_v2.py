print("正在运行 V2 版本的检查脚本...")
try:
    # 我们不直接导入整个 imagebind，而是尝试导入它内部一个具体的部分
    from imagebind import data
    import torch
    import pandas as pd

    print("\n🎉 V2 版本检查成功！ImageBind 和其他库都已正确安装并且可以被代码找到。")
    print(f"    - PyTorch (引擎) 版本: {torch.__version__}")
    print("    - ImageBind (大厨) 已就位!")

except ImportError as e:
    print(f"\n😭 V2 版本检查失败。错误信息是: {e}")
    print("这确认了Python确实无法找到ImageBind的安装。请看下面的终极解决方案。")