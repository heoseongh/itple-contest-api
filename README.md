# Contest API

공모전 정보를 뿌려주는 `Contest REST API` 개발 레포지터리 입니다.

## 사용 기술

- [ ] python
- [ ] DjangoRestFramework

## 클라이언트 구동 방법

### 파이썬 버전 확인

```bash
$ python --version
```

### git clone

```bash
$ git clone https://github.com/heoseongh/itple-contest-api.git
```

## 작업 정책

1. `main` 브랜치에서 작업하지 않는다.
2. 개발은 `dev` 브랜치에서 한다.
3. 특정 기능이나 서비스 개발은 `dev` 브랜치로부터 새로 브랜치를 생성하여 작업한다.

- 예) `contestpage`, `mypage`

4. 개발이 완료되면 `dev` 브랜치를 `main` 브랜치로 통합한다.

### dev 브랜치로 이동

```bash
$ git checkout dev
```

#### 이동 되었는지 확인 (`*`이 dev에 위치하면 된다.)

```bash
$ git branch
* dev
  main
```

### 각 기능별 브랜치 생성

```bash
$ git checktou -b contestpage
```

### 기능 구현 완료시 dev 브랜치로 merge

```bash
$ git checkout dev
$ git merge contestpage
```

### 최종 수정 후 main 브랜치로 merge

```bash
$ git checkout main
$ git merge dev
```
