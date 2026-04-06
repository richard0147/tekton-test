# tekton-test

用于验证 Tekton 流水线的小型示例仓库：两个独立子项目，各自包含最小可运行的 HTTP 服务与 Dockerfile。基础镜像统一从内部 Harbor 拉取：`harbor.haivivi.cn/library`。

## 目录结构

| 目录 | 说明 |
|------|------|
| `hello-python/` | Python 3.12，标准库 HTTP 服务 |
| `hello-node/` | Node.js 20，原生 `http` 模块 |

两个服务均监听 `8080`（可通过环境变量 `PORT` 覆盖），`GET /` 与 `GET /health` 返回纯文本响应，便于健康检查。

## 前置条件

- 已安装 Docker（或兼容的构建运行时）。
- 能够访问 `harbor.haivivi.cn`，且 Harbor 中已同步对应基础镜像标签（见各目录下 `Dockerfile` 的 `FROM`）。
- 若拉取镜像返回 **401**，需先登录：

```bash
docker login harbor.haivivi.cn
```

## 构建镜像

```bash
docker build -t tekton-test/hello-python:local ./hello-python
docker build -t tekton-test/hello-node:local ./hello-node
```

## 本地运行容器

```bash
docker run --rm -p 8080:8080 tekton-test/hello-python:local
docker run --rm -p 8080:8080 tekton-test/hello-node:local
```

另开终端：

```bash
curl -s http://127.0.0.1:8080/health
```

## 不经过 Docker 的本地调试

```bash
cd hello-python && python3 app.py
```

```bash
cd hello-node && node index.js
```

## 与 Tekton 的配合

将各子目录作为独立构建上下文（`context`）指向对应路径即可；流水线中需配置能拉取 `harbor.haivivi.cn` 的镜像凭据（如 `imagePullSecrets` 或 Kaniko/buildah 的 registry 认证）。
