from enum import Enum
from pydantic import BaseModel
from typing import Literal


class HashAlgo(str, Enum):
    sha256 = "sha256"


class Sibling(BaseModel):
    rfilename: str
    size: int


class DatasetInfo(BaseModel):
    id: str | None
    sha: str | None
    lastModified: str | None
    tags: list[str] | None
    siblings: list[Sibling] | None
    private: bool
    author: str | None
    description: str | None
    citation: str | None
    cardData: dict | None
    downloads: int = 0
    likes: int = 0


class ResponseWhoami(BaseModel):
    name: str


# create_repo
class RepoType(str, Enum):
    dataset = "dataset"
    space = "space"
    model = "model"


class RepoSdk(str, Enum):
    gradio = "gradio"
    streamlit = "streamlit"
    docker = "docker"
    static = "static"


class CreateRepoRequest(BaseModel):
    name: str
    type: RepoType = RepoType.model
    organization: str | None
    private: bool | None
    sdk: RepoSdk | None
    hardware: str | None


class CreateRepoResponse(BaseModel):
    error: str | None
    url: str


# list_repo_objects
class RepoObjectType(str, Enum):
    directory = "directory"
    file = "file"


class RepoObjectLfsInfo(BaseModel):
    oid: str
    size: int
    pointerSize: int


class RepoObjectCommit(BaseModel):
    id: str | None
    title: str | None
    date: str


class RepoObject(BaseModel):
    type: RepoObjectType
    oid: str
    size: int
    lfs: RepoObjectLfsInfo | None
    path: str
    lastCommit: RepoObjectCommit | None


# preupload_repository_files
class UploadFileInfo(BaseModel):
    path: str
    sample: str
    size: int
    sha: str


class PreuploadDatasetRequest(BaseModel):
    files: list[UploadFileInfo]


class UploadMode(str, Enum):
    lfs = "lfs"
    regular = "regular"


class PreuploadResponseFileInfo(BaseModel):
    path: str
    uploadMode: UploadMode
    shouldIgnore: bool = False


class PreuploadResponse(BaseModel):
    files: list[PreuploadResponseFileInfo]


# commit_repository_files
class CommitRequestOperationHeaderValue(BaseModel):
    summary: str
    description: str


class CommitRequestOperationHeader(BaseModel):
    key: Literal['header']
    value: CommitRequestOperationHeaderValue


class CommitRequestOperationDeleteFileValue(BaseModel):
    path: str


class CommitRequestOperationDeleteFile(BaseModel):
    key: Literal['deletedFile']
    value: CommitRequestOperationDeleteFileValue


class CommitRequestOperationFileValue(BaseModel):
    content: str
    path: str
    encoding: str | None


class CommitRequestOperationFile(BaseModel):
    key: Literal['file']
    value: CommitRequestOperationFileValue


class CommitLfsFileValue(BaseModel):
    path: str
    algo: HashAlgo
    oid: str
    size: int


class CommitRequestOperationLfsFile(BaseModel):
    key: Literal['lfsFile']
    value: CommitLfsFileValue


class CommitRequestOperation(BaseModel):
    __root__: CommitRequestOperationHeader | CommitRequestOperationFile | CommitRequestOperationDeleteFile | CommitRequestOperationLfsFile

    def __getattr__(self, attr):
        return getattr(self.__root__, attr)


class CommitResponse(BaseModel):
    success: bool
    commitOid: str
    commitUrl: str
    hookOutput: str


class CreateBranchRequest(BaseModel):
    startingPoint: str | None
